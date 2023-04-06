const calculateNumber = require('./utils.js');


module.exports = function sendPaymentRequestToApi(totalAmount, totalShipping){
  const a = calculateNumber('SUM', totalAmount, totalShipping);
  return `The total is: ${a}`;
}
