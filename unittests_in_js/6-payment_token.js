// Task 6, Async tests with done 🚰

function getPaymentTokenFromAPI(success) {
  return new Promise((resolve, reject) => {
    if (success) {
      resolve({data: 'Successful response from the API'});
    } else {
      // If success is false, don't do anything
      resolve();
    }
  });
}

module.exports = getPaymentTokenFromAPI;
