const express = require('express');
const AppController = requiire('../controllers/AppController');
const StudentsController = require('../controllers/StudentsController');

const router = express.Router();

router.get('/', AppController.getHompage);
router.get('/students', StudentsController.getAllStudents);
router.get('/students/:major', StudentsController.getAllStudentsByMajor);

module.exports = router;
