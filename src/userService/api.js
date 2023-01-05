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

    // See the rest of the methods in
    // https://github.com/Joker666/microservice-demo/blob/main/userService/api.js
};