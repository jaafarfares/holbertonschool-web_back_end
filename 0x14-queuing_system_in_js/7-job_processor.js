import kue from 'kue';

const queue = kue.createQueue();
const blacklistedNumbers = ['4153518780', '4153518781'];

queue.process('push_notification_code_2', 2, (job, done) => {
  const { phoneNumber, message } = job.data;

  const sendNotification = (phoneNumber, message, job, done) => {
    let progress = 0;

    const interval = setInterval(() => {
      job.progress(progress);

      if (progress === 50) {
        console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
      }

      if (progress === 100) {
        clearInterval(interval);
        done();
      }

      progress += 50;
    }, 50);

    if (blacklistedNumbers.includes(phoneNumber)) {
      clearInterval(interval);
      done(new Error(`Phone number ${phoneNumber} is blacklisted`));
    }
  };

  sendNotification(phoneNumber, message, job, done);
});
