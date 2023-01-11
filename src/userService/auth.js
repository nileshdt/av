const jwt = require('jsonwebtoken');

module.exports.generateToken = async (payload) => {
    return jwt.sign(payload, process.env.TOKEN_SECRET, { expiresIn: process.env.TOKEN_LIFE });
}

module.exports.verify = async (token, callback) => {
    console.log("auth verify");
    return jwt.verify(token, process.env.TOKEN_SECRET, async (err, user) => {
        if (err) {
            console.error(err);
        }
        //return user; //? callback(user) : callback(null);
        console.log(user);
        return user;
    });
}