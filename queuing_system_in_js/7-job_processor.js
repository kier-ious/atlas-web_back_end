import kue from 'kue';

const queue = kue.createQueue();

function sendNotification(phoneNumber, message, job, done) {
  job.progress(0, 100);

  if (!phoneNumber || !message) {
    done(new Error('Missing phone number or message'));
    return;
  }

  job.progress(50, 100);
  console.log(`Sending notification is ${phoneNumber}, with message: ${message}`);

  done();
}

queue.process('push_notification_code_2', 2, (job, done) => {
  sendNotification(job.data.phoneNumber, job.data.message, job, done);
});
