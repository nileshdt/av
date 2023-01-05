// userService/testClient.js

const messages = require('./proto/user_pb');
const services = require('./proto/user_grpc_pb');
const grpc = require('@grpc/grpc-js');

function main() {
    const client = new services.UserSvcClient('localhost:50055', grpc.credentials.createInsecure());
    console.log("Client created");
    console.log("Sending Register request");
    let registerReq = new messages.RegisterRequest();
    registerReq.setName("Hello");
    registerReq.setEmail("hello@world.com");
    registerReq.setPassword("Password");
    client.register(registerReq, function (err, response) {
        console.log(response);
    });

    console.log("Sending Login request");
    let loginReq = new messages.LoginRequest();
    loginReq.setEmail("hello@world.com");
    loginReq.setPassword("Password");
    client.login(loginReq, function (err, response) {
        console.log(response);
    });

    console.log("Sending Verify request");
    let verifyReq = new messages.VerifyRequest();
    verifyReq.setToken("eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJuYW1lIjoiSGVsbG8iLCJlbWFpbCI6ImhlbGxvQHdvcmxkLmNvbSIsInBhc3N3b3JkIjoiJDJiJDEwJFo0VS9XaEJjZjF0SlNRek1sd29XcU9pNlN2ejUueXF5dWF4MzdtU1cwc2tWTEdhbXdFd0UyIiwiX2lkIjoiNjNiNzQ1ZDNmYTkxZDI1MDhjNWI1YTcyIiwiaWF0IjoxNjcyOTU1MzQ4LCJleHAiOjE2NzY1NTUzNDh9.8KRkoa2t607FFb-xO5KSHZMS7xi9dNaEB1TaGVfM_qk");
    client.verify(verifyReq, function (err, response) {
        console.log(response);
    });


}

main();