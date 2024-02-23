const express = require('express');
const app = express();
const path = require('path');
const multer = require('multer');
const bodyParser = require('body-parser');
const fs = require('fs');
const { spawn } = require('child_process');
const port = 5000;

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
  
  //Run Question Generation
  const { spawn } = require('child_process');

  const pythonProcess = spawn('python3', ['C:/Hacked_Jan6/Metamorphosis/demogpt.py']);

  pythonProcess.stdout.on('data', (data) => {
    console.log(`stdout: ${data}`);
  });

  pythonProcess.stderr.on('data', (data) => {
    console.error(`stderr: ${data}`);
  });

  pythonProcess.on('close', (code) => {
    console.log(`Python script exited with code ${code}`);

    // Function to check if file exists
    function checkFileExists(filePath) {
      fs.access(filePath, fs.constants.F_OK, (err) => {
        if (err) {
          console.log('File not found. Waiting...');
          setTimeout(() => checkFileExists(filePath), 1000); // Check again after a delay
        } else {
          console.log('File found. Redirecting...');
          res.redirect('/interview1.html');
        }
      });
    }

    // Replace 'outputFile.txt' with the path to the file you're waiting for
    checkFileExists('C:/Hacked_Jan6/Metamorphosis/my-express-app/public/output_1.json');
  });

  pythonProcess.stdout.on('data', (data) => {
    console.log(`stdout: ${data}`);
  });

  pythonProcess.stderr.on('data', (data) => {
    console.error(`stderr: ${data}`);
  });
});

// Handle form submission POST request
app.post('/submit-form', (req, res) => {
    const { exec } = require('child_process');
    //Remove Previous Files
    exec('cd ./public/ && del output_1.json')
    exec('cd ./public/ && del output_2.json')
    exec('cd ./public/ && del output_3.json')
    exec('cd ./public/ && del output_4.json')
    exec('cd ./public/ && del output_5.json')
    exec('cd ./public/ && del output_6.json')
    exec('cd .. && del AnswerRecording1.mp4')
    exec('cd .. && del AnswerRecording2.mp4')
    exec('cd .. && del AnswerRecording3.mp4')
    exec('cd .. && del AnswerRecording4.mp4')
    exec('cd .. && del AnswerRecording5.mp4')
    exec('cd .. && del AnswerRecording6.mp4')
    exec('cd .. && del temp_audio1.wav')
    exec('cd .. && del temp_audio2.wav')
    exec('cd .. && del temp_audio3.wav')
    exec('cd .. && del temp_audio4.wav')
    exec('cd .. && del temp_audio5.wav')
    exec('cd .. && del temp_audio6.wav')
    exec('cd .. && del transcribed_text1.txt')
    exec('cd .. && del transcribed_text2.txt')
    exec('cd .. && del transcribed_text3.txt')
    exec('cd .. && del transcribed_text4.txt')
    exec('cd .. && del transcribed_text5.txt')
    exec('cd .. && del transcribed_text6.txt')
    exec('cd .. && del done.txt')
    exec('cd ./public/ && del FinalData.json')
    exec('cd .. && del CurrResume.pdf')
    exec('cd .. && del output.txt')
    exec('del FinalData.txt')
    const jobtitle = req.body.jobtitle;
    const description = req.body.description;

    const cleanJobTitle = jobtitle.replace(/[\r\n]+$/, '');
    const cleanDescription = description.replace(/[\r\n]+$/, '');

    // Create a string to save to the .txt file
    const content = `Job_Title = \'${cleanJobTitle}\'\nJob_Description = \'${cleanDescription}\'`;

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

app.post('/run-python-script1', (req, res) => {
  const pythonProcess = spawn('python3', ['C:/Hacked_Jan6/Metamorphosis/Mp4Convert1.py']);

  pythonProcess.stdout.on('data', (data) => {
      console.log(`stdout: ${data}`);
  });

  pythonProcess.stderr.on('data', (data) => {
      console.error(`stderr: ${data}`);
  });

  pythonProcess.on('close', (code) => {
      console.log(`Python script exited with code ${code}`);
      res.json({ message: 'Python script executed successfully' });
  });
});

app.post('/run-python-script2', (req, res) => {
  const pythonProcess = spawn('python3', ['C:/Hacked_Jan6/Metamorphosis/Mp4Convert2.py']);

  pythonProcess.stdout.on('data', (data) => {
      console.log(`stdout: ${data}`);
  });

  pythonProcess.stderr.on('data', (data) => {
      console.error(`stderr: ${data}`);
  });

  pythonProcess.on('close', (code) => {
      console.log(`Python script exited with code ${code}`);
      res.json({ message: 'Python script executed successfully' });
  });
});

app.post('/run-python-script3', (req, res) => {
  const pythonProcess = spawn('python3', ['C:/Hacked_Jan6/Metamorphosis/Mp4Convert3.py']);

  pythonProcess.stdout.on('data', (data) => {
      console.log(`stdout: ${data}`);
  });

  pythonProcess.stderr.on('data', (data) => {
      console.error(`stderr: ${data}`);
  });

  pythonProcess.on('close', (code) => {
      console.log(`Python script exited with code ${code}`);
      res.json({ message: 'Python script executed successfully' });
  });
});

app.post('/run-python-script4', (req, res) => {
  const pythonProcess = spawn('python3', ['C:/Hacked_Jan6/Metamorphosis/Mp4Convert4.py']);

  pythonProcess.stdout.on('data', (data) => {
      console.log(`stdout: ${data}`);
  });

  pythonProcess.stderr.on('data', (data) => {
      console.error(`stderr: ${data}`);
  });

  pythonProcess.on('close', (code) => {
      console.log(`Python script exited with code ${code}`);
      res.json({ message: 'Python script executed successfully' });
  });
});

app.post('/run-python-script5', (req, res) => {
  const pythonProcess = spawn('python3', ['C:/Hacked_Jan6/Metamorphosis/Mp4Convert5.py']);

  pythonProcess.stdout.on('data', (data) => {
      console.log(`stdout: ${data}`);
  });

  pythonProcess.stderr.on('data', (data) => {
      console.error(`stderr: ${data}`);
  });

  pythonProcess.on('close', (code) => {
      console.log(`Python script exited with code ${code}`);
      res.json({ message: 'Python script executed successfully' });
  });
});

app.post('/run-python-script6', (req, res) => {
  const pythonProcess = spawn('python3', ['C:/Hacked_Jan6/Metamorphosis/Mp4Convert6.py']);

  pythonProcess.stdout.on('data', (data) => {
      console.log(`stdout: ${data}`);
  });

  pythonProcess.stderr.on('data', (data) => {
      console.error(`stderr: ${data}`);
  });

  pythonProcess.on('close', (code) => {
      console.log(`Python script exited with code ${code}`);
      res.json({ message: 'Python script executed successfully' });
  });
});

app.post('/run-1st', (req, res) => {
  const pythonProcess = spawn('python3', ['C:/Hacked_Jan6/Metamorphosis/1st.py']);

  pythonProcess.stdout.on('data', (data) => {
      console.log(`stdout: ${data}`);
  });

  pythonProcess.stderr.on('data', (data) => {
      console.error(`stderr: ${data}`);
  });

  pythonProcess.on('close', (code) => {
      console.log(`Python script exited with code ${code}`);
      res.json({ message: 'Python script executed successfully' });
  });
});

app.post('/run-2nd', (req, res) => {
  const pythonProcess = spawn('python3', ['C:/Hacked_Jan6/Metamorphosis/2nd.py']);

  pythonProcess.stdout.on('data', (data) => {
      console.log(`stdout: ${data}`);
  });

  pythonProcess.stderr.on('data', (data) => {
      console.error(`stderr: ${data}`);
  });

  pythonProcess.on('close', (code) => {
      console.log(`Python script exited with code ${code}`);
      res.json({ message: 'Python script executed successfully' });
  });
});

app.post('/run-3rd', (req, res) => {
  const pythonProcess = spawn('python3', ['C:/Hacked_Jan6/Metamorphosis/3rd.py']);

  pythonProcess.stdout.on('data', (data) => {
      console.log(`stdout: ${data}`);
  });

  pythonProcess.stderr.on('data', (data) => {
      console.error(`stderr: ${data}`);
  });

  pythonProcess.on('close', (code) => {
      console.log(`Python script exited with code ${code}`);
      res.json({ message: 'Python script executed successfully' });
  });
});

app.post('/run-4th', (req, res) => {
  const pythonProcess = spawn('python3', ['C:/Hacked_Jan6/Metamorphosis/4th.py']);

  pythonProcess.stdout.on('data', (data) => {
      console.log(`stdout: ${data}`);
  });

  pythonProcess.stderr.on('data', (data) => {
      console.error(`stderr: ${data}`);
  });

  pythonProcess.on('close', (code) => {
      console.log(`Python script exited with code ${code}`);
      res.json({ message: 'Python script executed successfully' });
  });
});

app.post('/run-5th', (req, res) => {
  const pythonProcess = spawn('python3', ['C:/Hacked_Jan6/Metamorphosis/5th.py']);

  pythonProcess.stdout.on('data', (data) => {
      console.log(`stdout: ${data}`);
  });

  pythonProcess.stderr.on('data', (data) => {
      console.error(`stderr: ${data}`);
  });

  pythonProcess.on('close', (code) => {
      console.log(`Python script exited with code ${code}`);
      res.json({ message: 'Python script executed successfully' });
  });
});

app.post('/run-6th', (req, res) => {
  const pythonProcess = spawn('python3', ['C:/Hacked_Jan6/Metamorphosis/6th.py']);

  pythonProcess.stdout.on('data', (data) => {
      console.log(`stdout: ${data}`);
  });

  pythonProcess.stderr.on('data', (data) => {
      console.error(`stderr: ${data}`);
  });

  pythonProcess.on('close', (code) => {
      console.log(`Python script exited with code ${code}`);
      // Do not send a response here
      checkFileExists('C:/Hacked_Jan6/Metamorphosis/done.txt');
    });

  function checkFileExists(filePath) {
    fs.access(filePath, fs.constants.F_OK, (err) => {
        if (err) {
            console.log('File not found. Waiting...');
            setTimeout(() => checkFileExists(filePath), 1000);
        } else {
            console.log('File found.');
            const { exec } = require('child_process');
            exec('copy FinalData.txt C:\\Hacked_Jan6\\Metamorphosis\\my-express-app\\public\\FinalData.json')
            res.json({ redirect: '/results-and-counter1.html' }); // Send JSON response with redirect URL
        }
    });
  }

});

app.use(express.static('public')); // Serve static files


app.listen(port, () => {
  console.log(`Server listening at http://localhost:${port}`);
});
