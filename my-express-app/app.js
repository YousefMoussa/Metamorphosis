const express = require('express');
const app = express();
const path = require('path');
const multer = require('multer');
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
  res.sendFile(path.join(__dirname, 'public', 'dhruvhtmltest.html'));
});

// Handle file upload POST request
app.post('/upload', upload.single('pdfFile'), (req, res) => {
  // 'pdfFile' is the name attribute in your HTML file input
  console.log(req.file); // Information about the uploaded file
  res.send('File uploaded successfully');
});

app.listen(port, () => {
  console.log(`Server listening at http://localhost:${port}`);
});