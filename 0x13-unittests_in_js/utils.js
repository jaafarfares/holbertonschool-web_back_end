module.exports = class Utils {
    calculateNumber(type, a, b) {
        if (typeof a !== 'number' || typeof b !== 'number') {
          throw new TypeError('Parameters must be numbers');
        }
        let result;
      
        switch (type) {
          case 'SUM':
            result = Math.round(a) + Math.round(b);
            break;
          case 'SUBTRACT':
            result = Math.round(a) - Math.round(b);
            break;
          case 'DIVIDE':
            if (Math.round(b) === 0) {
              result = 'Error';
            } else {
              result = Math.round(a) / Math.round(b);
            }
            break;
          default:
            throw new Error('Invalid type');
        }
      
        return result;
      }

 }
