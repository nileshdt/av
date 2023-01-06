// userService/testClient.js

const messages = require('./proto/user_pb');
const services = require('./proto/user_grpc_pb');
const grpc = require('@grpc/grpc-js');

function main() {
    const client = new services.UserSvcClient('localhost:50051', grpc.credentials.createInsecure());
    console.log("Client created");
    console.log("Sending Register request");
    token = ""
    let email = "hello@world.com"
    let password = "Password"
    let registerReq = new messages.RegisterRequest();
    registerReq.setName("Hello");
    registerReq.setEmail(email);
    registerReq.setPassword(password);
    client.register(registerReq, function (err, response) {
        console.log("Register response");
        token = response.getToken();
        //console.log(token);
    });

    console.log("Sending Login request");
    let loginReq = new messages.LoginRequest();
    loginReq.setEmail(email);
    loginReq.setPassword(password);
    client.login(loginReq, function (err, response) {

        console.log("Login response");
        token=  response.getToken();
        console.log(response.getToken());

    });

    token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJfaWQiOiI2M2I3ODBjNmI4MjYyZTMzZTUwZGU3NzgiLCJuYW1lIjoiSGVsbG8iLCJlbWFpbCI6ImhlbGxvQHdvcmxkLmNvbSIsInBhc3N3b3JkIjoiJDJiJDEwJFc3TXBWbFVBVTlPWWpjaDIvTVV5Y2U0cDdLZmNNWVJENEhlNjJlQXo3dVcvb3RVa2kyREZ1IiwiaWF0IjoxNjcyOTcyNTgwLCJleHAiOjE2NzY1NzI1ODB9.DwkJDKhrJDJufpe7EZKifR5HWKL_dqhENBiwXKy1nBM"
    console.log("Sending Verify request");
    console.log(token);

    let verifyReq = new messages.VerifyRequest();
    verifyReq.setToken(token);
    client.verify(verifyReq, function (err, response) {
        console.log("verify response");
        console.log(err)
        console.log(response);
    });


}

main();