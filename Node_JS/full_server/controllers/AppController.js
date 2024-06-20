class AppController {
  static getHomepage(res, req) {
    res.status(200).send('Hello Holberton School!');
  }
}

module.exports = AppController;
