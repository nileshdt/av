// userService/testClient.js

const messages = require('./proto/user_pb');
const services = require('./proto/user_grpc_pb');
const grpc = require('@grpc/grpc-js');

async function main() {
    const client = new services.UserSvcClient('localhost:50055', grpc.credentials.createInsecure());
    console.log("Client created");
    console.log("Sending Register request");
    token = ""
    let email = "hello@world.com"
    let password = "Password"
    let registerReq = new messages.RegisterRequest();
    registerReq.setName("Hello");
    registerReq.setEmail(email);
    registerReq.setPassword(password);
    await client.register(registerReq, function (err, response) {
        console.log("Register response");
        if (err) {
            console.error(err);
        }
        token = response.getToken();
        console.log(token);
    });

    console.log("Sending Login request");
    let loginReq = new messages.LoginRequest();
    loginReq.setEmail(email);
    loginReq.setPassword(password);
    await client.login(loginReq, function (err, response) {
        console.log("Login response");
        if (err) {
            console.error(err);
        }
        token = response.getToken();
        console.log(token);

    });

    token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJfaWQiOiI2M2I3M2Y2NmZkMThlNDUwNWI0NzNhYTciLCJuYW1lIjoiSGVsbG8iLCJlbWFpbCI6ImhlbGxvQHdvcmxkLmNvbSIsInBhc3N3b3JkIjoiJDJiJDEwJEpwRjRjWnFrMnluZFRrSzhkN3pKTC5vczRUR0ZONmdnMUZOU1phcHhMWjR5WXNsLm02UDgyIiwiaWF0IjoxNjczMDMxMjkzLCJleHAiOjE2NzY2MzEyOTN9.Pon7GHZXrfACC_tw-2cNDpsCobxWgB_ehKGSWRxeCdg"
    console.log("Sending Verify request");
    console.log(token);

    let verifyReq = new messages.VerifyRequest();
    console.log(1);
    verifyReq.setToken(token);
    console.log(2);
    console.log(verifyReq.getToken());
    await client.verify(verifyReq, function (err, response) {
        console.log("verify response1");
        if (err) {
            console.error(err);
        }
        console.log(response);
    });
}
main();