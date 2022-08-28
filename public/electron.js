const electron = require("electron");
const app = electron.app;
const BrowserWindow = electron.BrowserWindow;
const path = require("path");
const isDev = require("electron-is-dev");
const {PythonShell} = require('python-shell');

let mainWindow;

function createWindow() {
    mainWindow = new BrowserWindow({ 
        width: 1200, 
        height: 800,
        icon: "",
		autoHideMenuBar: true
    });
     
	//let pyshell = new PythonShell(`${path.join(__dirname, "../src/script/IA/main.py")}`)
	
	//para adicionar coisas no python pyshell.send(JSON.stringify([10]))
	
	//pyshell.on('message', function(message) {
	//  console.log(message);
	//})
	
	//pyshell.end(function (err) {
	//  if (err){
	//	throw err;
	//  };
	//  console.log('finished');
	//});

    mainWindow.loadURL(
        isDev
        ? "http://localhost:3000"
        : `file://${path.join(__dirname, "../build/index.html")}`
    );
    mainWindow.on("closed", () => (mainWindow = null));
}

app.on("ready", () => {
	createWindow();
});

app.on("window-all-closed", () => {
    if (process.platform !== "darwin") {
    app.quit();
    }
});

app.on("activate", () => {
    if (mainWindow === null) {
    createWindow();
    }
});