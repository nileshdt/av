const grpc = require('grpc-js');
const Mali = require('mali');
const MongoClient = require('mongodb').MongoClient;

// Connect to the MongoDB database
const uri = 'mongodb://localhost:27017';
const client = new MongoClient(uri, { useNewUrlParser: true });
client.connect((err) => {
    if (err) {
        console.log(err);
        process.exit(1);
    }
    // Create a Mali app
    const app = new Mali('localhost:50054');

    // Define a simple gRPC service with a single sayHello method
    app.use({
        sayHello: async (ctx) => {
            const name = ctx.req.name;
            console.log(`Received request to say hello to ${name}`);

            // Use the MongoDB driver to insert a document into the "names" collection
            const result = await client.db('test').collection('names').insertOne({ name });
            console.log(`Inserted ${result.insertedCount} documents into the "names" collection`);

            // Send a response back to the client using the grpc-js library
            ctx.res = { message: `Hello, ${name}!` };
            grpc.send(ctx.res);
        },
    });
    // Start the Mali app
    app.start();
    console.log('gRPC server listening on localhost:50054');
});    