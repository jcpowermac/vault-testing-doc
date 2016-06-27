var options = {
  apiVersion: 'v1', // default
  endpoint: 'http://vault:8200', // default
  token: '1234' // client token; can be fetched after valid initialization of the server
};

// get new instance of the client
var vault = require("node-vault")(options);

// init vault server
vault.init({ secret_shares: 5, secret_threshold: 3 }, function(err, result) {
  var keys = result.keys;
  vault.token = result.root_token;
  // unseal vault server
  vault.unseal({ secret_shares: 3, key: keys[0] }, function(err, result) {});
  vault.unseal({ secret_shares: 3, key: keys[1] }, function(err, result) {});
  vault.unseal({ secret_shares: 3, key: keys[2] }, function(err, result) {});
});