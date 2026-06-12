> **⚠️ ARCHIVED PROJECT**  
> This project is archived and now part of my [Automation-Toolbox](https://github.com/sadmanhsakib/Automation-Toolbox) repository.

# Browser Bookmark Backup Utility

## Overview

This utility provides automated backup functionality for Chromium-based browser bookmarks. The script extracts bookmark data from browser-native JSON storage and exports it to standards-compliant HTML bookmark format files. Backup rotation is implemented to manage storage consumption.

## Operational Characteristics

### Supported Browser Formats

The utility operates on Chromium bookmark JSON structures. Compatibility extends to:

- Google Chrome
- Microsoft Edge
- Brave Browser
- Opera
- Vivaldi
- Other Chromium derivatives

### Backup Scope

The script processes two bookmark categories per browser profile:

1. **Bookmark Bar**: Primary user-facing bookmark toolbar
2. **Other Bookmarks**: Secondary bookmark storage location

Bookmark hierarchy, including nested folder structures, is preserved in the exported HTML.

## Technical Implementation

### Data Processing Pipeline

1. **Source Ingestion**: JSON bookmark files are parsed using Python's standard `json` module
2. **Recursive Extraction**: Bookmark folder trees are traversed recursively to maintain hierarchical relationships
3. **Format Conversion**: Bookmarks are transformed to Netscape Bookmark File Format 1 (HTML)
4. **File Generation**: Output files are written with UTF-8 encoding to ensure international character support
5. **Rotation Management**: Backup files exceeding the configured retention limit are removed in chronological order

### Execution Model

The script is implemented as a Python Windows script (`.pyw` extension), enabling silent execution without console window instantiation. This design accommodates scheduled task automation without user interface interruption.

## Configuration Requirements

### Environment Variables

Configuration is managed through environment variables loaded from a `.env` file. The following parameters must be defined:

| Variable | Required | Description | Constraints |
|----------|------|-------------|-------------|
| `BOOKMARK_DIRS` | MUST | Comma-separated absolute paths to browser bookmark JSON files | Must be valid file paths with read permissions |
| `OUTPUT_DIR` | Optional | Absolute path for backup file storage | Directory must be writable; created if nonexistent |
| `MAX_BACKUP` | Optional | Maximum number of backup files to retain per browser | Set to `0` for unlimited retention |

### Configuration Template

A configuration template is provided in `example.env`:

```
BOOKMARK_DIRS=
OUTPUT_DIR=
MAX_BACKUP=
```

### Locating Browser Bookmark Files

Bookmark JSON files are typically located at the following system paths:

**Google Chrome / Microsoft Edge / Brave:**
```
%LOCALAPPDATA%\{BrowserVendor}\{BrowserName}\User Data\Default\Bookmarks
```

**Example Paths:**
```
C:\Users\{Username}\AppData\Local\Google\Chrome\User Data\Default\Bookmarks
C:\Users\{Username}\AppData\Local\Microsoft\Edge\User Data\Default\Bookmarks
C:\Users\{Username}\AppData\Local\BraveSoftware\Brave-Browser\User Data\Default\Bookmarks
```

### Configuration Example

```env
BOOKMARK_DIRS=C:\Users\JDoe\AppData\Local\Google\Chrome\User Data\Default\Bookmarks,C:\Users\JDoe\AppData\Local\Microsoft\Edge\User Data\Default\Bookmarks
OUTPUT_DIR=D:\Backups\Bookmarks
MAX_BACKUP=30
```

## Installation

### Prerequisites

- Python 3.7 or higher
- `python-dotenv` package

### Dependency Installation

```bash
pip install python-dotenv
```

### Repository Setup

1. Clone or download the repository
2. Copy `example.env` to `.env`
3. Configure environment variables in `.env`
4. Verify bookmark file paths and permissions

## Execution

### Manual Execution

```bash
python main.pyw
```

### Automated Scheduling (Windows Task Scheduler)

The utility is designed for unattended operation via Windows Task Scheduler:

1. Open Task Scheduler (`taskschd.msc`)
2. Create a new task with the following configuration:
   - **Trigger**: Daily or at system startup (as required)
   - **Action**: Start a program
   - **Program/script**: `pythonw.exe` (for windowless execution)
   - **Arguments**: `"D:\scripts\bookmark-backup\main.pyw"` (adjust path accordingly)
   - **Start in**: `D:\scripts\bookmark-backup` (script directory)
3. Configure task to run whether user is logged in or not
4. Set highest privileges if bookmark files require elevated access

## Output Specification

### File Naming Convention

Backup files are named according to the following pattern:

```
bookmark_backup_{index}_{YYYY-MM-DD}.html
```

- `{index}`: Sequential identifier when multiple bookmark sources are configured (1-based indexing)
- `{YYYY-MM-DD}`: ISO 8601 date format representing backup creation date

### HTML Format Compliance

Output files conform to the Netscape Bookmark File Format, ensuring compatibility with:

- All major web browsers (Chrome, Firefox, Safari, Edge, Opera)
- Bookmark management utilities
- Cross-platform bookmark synchronization tools

## Security Considerations

### Credential Exposure Risk

Browser bookmark files may contain URLs with embedded credentials (e.g., `https://user:password@example.com`). Organizations should assess exposure risk before deploying this utility in shared or cloud-synced storage environments.

### File System Permissions

- The `.env` configuration file contains sensitive file paths and should be excluded from version control
- Output directory access should be restricted to authorized users
- Backup files should be protected with appropriate file system ACLs

### Data Residency

Backup files are stored locally. No network transmission or external service integration is performed by the utility.

## Limitations and Known Constraints

1. **Browser Lock State**: The script does not verify whether source bookmark files are locked by running browser instances. Chromium browsers typically allow read access during operation, but data consistency is not guaranteed.

2. **Atomic Write Operations**: File write operations are not atomic. System failure during execution may result in incomplete backup files.

3. **Error Handling**: The implementation does not include comprehensive error handling for:
   - Missing or inaccessible source files
   - Insufficient disk space
   - Invalid JSON structures
   - Permission denial on output directory

4. **Bookmark Metadata Loss**: The following metadata is not preserved in HTML export:
   - Bookmark favicons
   - Creation/modification timestamps (beyond date in filename)
   - Custom bookmark properties
   - Browser-specific extensions

5. **Concurrent Execution**: The script does not implement file locking. Concurrent executions may result in race conditions during backup rotation.

6. **Character Encoding**: While UTF-8 encoding is specified, special characters in bookmark titles or URLs are not escaped for HTML entities. This may cause rendering issues with certain character sets.

## Operational Recommendations

1. **Backup Verification**: Periodic validation of backup file integrity is recommended through manual import testing
2. **Retention Policy**: Configure `MAX_BACKUP` based on available storage and regulatory retention requirements
3. **Monitoring**: Implement external monitoring for script execution failures when deployed in scheduled automation
4. **Browser Closure**: For maximum data consistency, configure scheduled tasks to execute when browsers are closed
5. **Differential Backup**: The utility does not implement differential or incremental backup. Each execution produces a complete snapshot

## Dependency Management

The utility requires the following Python package:

- **python-dotenv** (>=0.19.0): Environment variable management

No transitive dependencies with known critical vulnerabilities at time of documentation.

## License

This software is distributed under the MIT License. See `LICENSE` file for complete terms.

The software is provided "as is" without warranty of any kind, express or implied, including but not limited to the warranties of merchantability, fitness for a particular purpose, and noninfringement.

## Support and Maintenance

This utility is provided as a standalone script without guaranteed support or maintenance commitments. Organizations deploying this utility should:

1. Conduct internal code review prior to production deployment
2. Establish internal ownership for maintenance and security updates
3. Implement appropriate testing procedures
4. Document any modifications to the source code

## Version Information

- **Script Version**: Not versioned (single-file utility)
- **Python Compatibility**: 3.7+
- **Platform**: Windows (adaptable to POSIX systems with path modifications)
- **Last Updated**: 2025 (per license file)

---

For questions regarding implementation details or modification requirements, refer to the source code documentation in `main.pyw`.
