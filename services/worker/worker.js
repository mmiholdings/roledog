const Queue = require('bull');
const workQueue = new Queue('tasks', { redis: { host: process.env.REDIS_HOST || 'localhost' } });
console.log("Worker started, waiting for jobs...");
workQueue.process(async job => {
  console.log("Processing", job.id, job.data);
  return true;
});
