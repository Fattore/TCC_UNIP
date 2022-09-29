const electron = require("electron");
const app = electron.app;
const BrowserWindow = electron.BrowserWindow;

const path = require("path");
const isDev = require("electron-is-dev");
const { spawn } = require("child_process");
const ipcMain = electron.ipcMain;

const { io } = require("socket.io-client");
const socket = io("http://0.0.0.0:5000");
let mainWindow;

ipcMain.on("msg", (event, data)=> {
    socket.emit('get-data-python', data, (err, res) => {
        console.log(res)
        var result = res;

        ipcMain.on('request-from-relatorio', function(event, arg) {
            event.sender.send('response-to-relatorio', result);
        });
    })
})


function spawnPython(){
    let py = spawn('python', [`${path.join(__dirname, "../src/script/IA/main.py")}`])
    
    py.stdout.on("data", (data) => {
        console.log(`stdout: ${data}`)
    })

    py.stderr.on("data", (data) => {
        console.log(`error: ${data}`)
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

    spawnPython();
 
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