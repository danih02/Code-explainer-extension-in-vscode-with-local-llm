import * as vscode from 'vscode';
import axios from 'axios';

export function activate(context: vscode.ExtensionContext) {
    let disposable = vscode.commands.registerCommand('extension.explainCode', async () => {
        const editor = vscode.window.activeTextEditor;
        if (editor) {
            const code = editor.document.getText(editor.selection);
            if (code) {
                try {
                    const response = await axios.post('http://127.0.0.1:8000/explain', {
                        code: code
                    });
                    vscode.window.showInformationMessage(response.data.explanation);
                } catch (error) {
                    vscode.window.showErrorMessage('Error explaining code: ' + error.message);
                }
            } else {
                vscode.window.showWarningMessage('No code selected.');
            }
        }
    });

    context.subscriptions.push(disposable);
}

export function deactivate() {}