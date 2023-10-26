import kue from 'kue';
import createPushNotificationsJobs from './8-job';
import chai from 'chai';
import chaiAsPromised from 'chai-as-promised';

chai.use(chaiAsPromised);
chai.should();


const queue = kue.createQueue();

describe('createPushNotificationsJobs', () => {
  before(() => {
    queue.testMode.enter();
  });

  after(() => {
    queue.testMode.clear();
    queue.testMode.exit();
  });

  it('should display an error message if jobs is not an array', () => {
    try {
      createPushNotificationsJobs('not an array', queue);
    } catch (error) {
      const errorMessage = 'Jobs is not an array';
      error.message.should.equal(errorMessage);
    }
  });

  it('should create two new jobs to the queue', () => {
    const jobs = [
      { phoneNumber: '123', message: 'Message 1' },
      { phoneNumber: '456', message: 'Message 2' },
    ];

    createPushNotificationsJobs(jobs, queue);

    const jobsInQueue = queue.testMode.jobs;
    jobsInQueue.length.should.equal(2);

    jobsInQueue[0].type.should.equal('push_notification_code_3');
    jobsInQueue[1].type.should.equal('push_notification_code_3');
  });
});
