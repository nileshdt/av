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

    register = (call, callback) => {
        const users = this.db.collection("users");

        bcrypt.hash(call.request.getPassword(), 10, (err, hash) => {
            let user = { name: call.request.getName(), email: call.request.getEmail(), password: hash }
            users.insertOne(user).then(r => {
                let resp = new messages.UserResponse();
                resp.setId(user._id.toString());
                resp.setName(user.name);
                resp.setEmail(user.email);
                resp.setToken(auth.generateToken(user));
                callback(null, resp);
            });
        });
    }
    login = (call, callback) => {
        const users = this.db.collection("users");
        console.log(call.request.getEmail());
        users = users.find({ email: call.request.getEmail() }).toArray().then(users => {
            if (users.length > 0) {
                let user = users[0];
                bcrypt.compare(call.request.getPassword(), user.password, (err, result) => {
                    if (result) {
                        let resp = new messages.UserResponse();
                        resp.setId(user._id.toString());
                        resp.setName(user.name);
                        resp.setEmail(user.email);
                        resp.setToken(auth.generateToken(user));
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
    verify = (call, callback) => {
        let user = auth.verify(call.request.getToken());
        if (user) {
            let resp = new messages.UserResponse();
            resp.setId(user._id.toString());
            resp.setName(user.name);
            resp.setEmail(user.email);
            resp.setToken(auth.generateToken(user));
            callback(null, resp);
        } else {
            callback(new Error("Invalid token"), null);
        }
    }



    // See the rest of the methods in
    // https://github.com/Joker666/microservice-demo/blob/main/userService/api.js
};