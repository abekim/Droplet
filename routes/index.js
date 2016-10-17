const express = require('express');

const router = express.Router(); // eslint-disable-line new-cap

/* GET home page. */
router.get('/', (req, res, next) => {
  res.render('index', { title: 'Express' });
});

module.exports = router;
module.exports.user = require("./users");
