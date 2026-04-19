> **⚠️ ARCHIVED PROJECT**  
> This project is archived and now part of my [Automation-Toolbox](https://github.com/sadmanhsakib/Automation-Toolbox) repository.

# bookmark-backup

A lightweight Python utility that automatically backs up Chromium-based browser bookmarks (Brave, Chrome, Edge, etc.) to a portable HTML format while preserving the folder hierarchy.

## 📖 Overview

Browsers typically store bookmarks in a local JSON file that isn't directly usable for importing into other browsers or easy reading. **Auto-Bookmark-Backup** parses this internal JSON file and converts it into a standard `Netscape Bookmark File` (HTML) format.

This script is designed to run silently in the background (`.pyw`), making it perfect for automated, scheduled backups to ensure you never lose your important links.

## ✨ Key Features

-   **Universal Compatibility**: Converts proprietary JSON bookmarks into standard HTML importable by any web browser.
-   **Hierarchy Preservation**: Maintains your exact folder structure and nesting order.
-   **Silent Operation**: Runs without opening a terminal window, ideal for background tasks.
-   **Automation Ready**: Designed to be used with Windows Task Scheduler for "set it and forget it" backups.

## 🌍 Real-World Use Cases

1.  **Automated Safety Net**: Schedule the script to run weekly. If your browser profile gets corrupted or you accidentally delete a folder, you have a recent, restore-ready backup.
2.  **Browser Migration**: Easily move your bookmarks from one Chromium browser (e.g., Brave) to another (e.g., Firefox or Safari) without relying on cloud sync.
3.  **Versioned Backups**: Use this script in a Dropbox/OneDrive folder or a Git repository to keep a history of how your bookmarks have changed over time.

## 🛠️ Prerequisites

-   **Python 3.x** installed on your system.
-   **`python-dotenv`** library for managing configuration.

## 🚀 Installation & Setup

1.  **Clone the Repository**
    ```bash
    git clone https://github.com/yourusername/bookmark-backup.git
    cd bookmark-backup
    ```

2.  **Install Dependencies**
    ```bash
    pip install python-dotenv
    ```

3.  **Configure the Path**
    Create a file named `.env` in the project directory. Add the path to your browser's `Bookmarks` file.

    **Example `.env` file:**
    ```env
    BOOKMARK_PATH="C:/Users/YourName/AppData/Local/BraveSoftware/Brave-Browser/User Data/Default/Bookmarks"
    ```
    > **Tip**: You can find your specific path by searching online for "Where does [Your Browser] store bookmarks?"

## 💻 Usage

### Manual Run
Simply double-click `main.pyw` or run it via terminal:
```bash
python main.pyw
```
This will generate a file named `bookmark_backup_[COUNT]_[DATE].HTML` in the same directory.

### Automated Backup (Recommended)
To ensure your bookmarks are always safe, set up a Windows Task Scheduler task:

1.  Open **Task Scheduler**.
2.  Click **Create Basic Task** and name it "Bookmark Backup".
3.  Set the **Trigger** (e.g., Weekly, every Friday).
4.  Set the **Action** to "Start a program".
5.  Browse and select the `main.pyw` file.
    *   *Note: In the "Start in (optional)" field, paste the full path to the script's folder to ensure it finds the `.env` file.*

## 📄 License

This project is open-source and available for personal and educational use.
