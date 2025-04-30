const { exec } = require("child_process");

// Simulate unsafe code
exec("ls", (err, stdout, stderr) => {
  if (err) {
    console.error(err);
    return;
  }
  console.log(stdout);
});
