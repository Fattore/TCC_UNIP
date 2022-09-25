const electron = require("electron");
const app = electron.app;
const BrowserWindow = electron.BrowserWindow;

const path = require("path");
const isDev = require("electron-is-dev");
const {PythonShell} = require('python-shell');
const { spawn } = require("child_process");
const ipcMain = electron.ipcMain;

const { io } = require("socket.io-client");
const socket = io("http://0.0.0.0:5000");
let mainWindow;


ipcMain.on("msg", (event, data)=> {
    spawnPython(data)
    socket.emit('get-data-python', 'Test data from the UI', (err, res) => {
        ipcMain.send("fromPython", res)
    })
})

function spawnPython(data){
    let py = spawn('python', [`${path.join(__dirname, "../src/script/IA/main.py")}`,data])
   
    py.stdout.on("data", (data) => {
        console.log(`stdout: ${data}`)
    })

    py.stderr.on("data", (data) => {
        console.log(`stdout: ${data}`)
    })

    py.on("close", (code) => {
        console.log(`close: ${code}`)
    })
}

function createWindow() {
    mainWindow = new BrowserWindow({ 
        width: 1200, 
        height: 800,
        icon: "",
		autoHideMenuBar: true,
        webPreferences:{
            nodeIntegration: true,
        }
    });
 
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