const express = require('express');
const app = express();
const path = require('path');
const multer = require('multer');
const bodyParser = require('body-parser');
const fs = require('fs');
const port = 3000;

// Set up storage location and filename for multer
const storage = multer.diskStorage({
  destination: function (req, file, cb) {
    cb(null, 'C:/Hacked_Jan6/Metamorphosis'); // Your desired upload directory
  },
  filename: function (req, file, cb) {
    // Create a custom file name
    const customFileName = 'CurrResume.pdf';
    cb(null, customFileName);
  }
});

const upload = multer({ storage: storage });

// Serve static files from the 'public' directory
app.use(express.static(path.join(__dirname, 'public')));

app.get('/', (req, res) => {
  res.sendFile(path.join(__dirname, 'public', 'homepage.html'));
  //res.sendFile(path.join(__dirname, 'public', 'dhruvhtmltest.html'));
});

// Middleware for parsing application/x-www-form-urlencoded
app.use(bodyParser.urlencoded({ extended: true }));

// Handle file upload POST request
app.post('/upload', upload.single('pdfFile'), (req, res) => {
  // 'pdfFile' is the name attribute in your HTML file input
  console.log(req.file); // Information about the uploaded file
  //res.send('File uploaded successfully');
  res.redirect('/interview.html');
});

// Handle form submission POST request
app.post('/submit-form', (req, res) => {
    const jobtitle = req.body.jobtitle;
    const description = req.body.description;

    // Create a string to save to the .txt file
    const content = `Job_Title = \'${jobtitle}\'\nJob_Description = \'${description}\'`;

    // Write to a .txt file
    fs.writeFile('C:/Hacked_Jan6/Metamorphosis/DetailsAndRole.py', content, (err) => {
        if (err) {
            console.error(err);
            return res.send('An error occurred while writing to the file.');
        }
        //res.send('Form data received and file written.');
        res.redirect('/resume.html');
    });
});

app.listen(port, () => {
  console.log(`Server listening at http://localhost:${port}`);
});
