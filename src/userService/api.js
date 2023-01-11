// userService/api.js

const bcrypt = require('bcrypt');
const auth = require("./auth");
const messages = require('./proto/user_pb');
const ObjectId = require('mongodb').ObjectID;

module.exports = class API {
    constructor(db, grpc) {
        this.db = db;
        this.grpc = grpc;
    }

    register = async (call, callback) => {
        console.log("register");
        const users = await this.db.collection("users");

        bcrypt.hash(call.request.getPassword(), 10, async (err, hash) => {
            let user = { name: call.request.getName(), email: call.request.getEmail(), password: hash }
            await users.insertOne(user).then(async r => {
                let resp = new messages.UserResponse();
                resp.setId(user._id.toString());
                resp.setName(user.name);
                resp.setEmail(user.email);
                resp.setToken(await auth.generateToken(user))
                callback(null, resp);
            });
        });
    }
    login = async (call, callback) => {
        let users = this.db.collection("users");
        console.log(call.request.getEmail());
        users = await users.find({ email: call.request.getEmail() }).toArray().then(async users => {
            if (users.length > 0) {
                let user = users[0];
                bcrypt.compare(call.request.getPassword(), user.password, async (err, result) => {
                    if (result) {
                        let resp = new messages.UserResponse();
                        resp.setId(user._id.toString());
                        resp.setName(user.name);
                        resp.setEmail(user.email);
                        resp.setToken(await auth.generateToken(user));
                        callback(null, resp);
                    } else {
                        callback(new Error("Invalid credentials"), null);
                    }
                });
            } else {
                callback(new Error("Invalid credentials"), null);
            }
        });
    }
    verify = async (call, callback) => {
        console.log("Verify");
        console.log(call.request.getToken());
        let user = await auth.verify(call.request.getToken());

        console.log(1);
        console.log(user);

        if (user) {
            let resp = new messages.VerifyResponse();
            resp.setId(user._id.toString());
            resp.setName(user.name);
            resp.setEmail(user.email);
            console.log(2);
            //resp.setToken(await auth.generateToken(user));
            //resp.setToken(call.request.getToken());
            callback(null, resp);
        } else {
            callback(new Error("Invalid token"), null);
        }

    }



    // See the rest of the methods in
    // https://github.com/Joker666/microservice-demo/blob/main/userService/api.js
};