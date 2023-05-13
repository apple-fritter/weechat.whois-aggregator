# WHOIS aggregation
Save `whois` data for an IRC user to a rolling `CSV` file using the WeeChat Python API.

The script requires the `WeeChat IRC client` to be installed and running, as well as `Python` 2 or 3 with the `WeeChat Python API` installed.

The script creates a CSV file in the user's home directory named `weechat_whois.csv`. If the file does not exist, the script creates it and writes a header row to the file with the column names. If the file already exists, the script appends the new data to the end of the file.

To use the script, you can type `/whois_to_csv <nick>` in a WeeChat buffer to save the whois data for a specific user to the CSV file. If no nick is provided, the script will save the whois data for the user currently selected in the buffer.

## Concerns
1. Script saves sensitive information such as the user's host and real name to a file without any encryption or security measures. If an attacker gains access to the system or the file, they could potentially obtain this information and use it maliciously.
2. The file is saved in a predictable location (i.e. the user's home directory), which could make it easier for an attacker to locate and exploit the file.
3. Script saves the data in a rolling CSV file, which could potentially fill up the user's hard drive over time if the script is used frequently and the user forgets to periodically delete old data. This could cause performance issues and potentially lead to system crashes.

## Potential uses
This script could be useful for logging whois data for various IRC users over time. For example, a user may want to keep track of changes in the host, real name, or username of specific users on a particular IRC network. By running this script regularly, they can store this information in a CSV file that can be easily parsed and analyzed later. Additionally, this script could be useful for moderators or administrators of IRC channels who want to keep track of changes in user information for security or administrative purposes.

## IRC Meta

### WeeChat
- [weechat.ban-evasion-detection](https://github.com/apple-fritter/weechat.ban-evasion-detection): Detect and prevent ban evasion. (Python)
- [weechat.typo-aggregator](https://github.com/apple-fritter/weechat.typo-aggregator): Record misspelled words in a TSV (tab-separated values) file. (Python)
- [weechat.whois-aggregator](https://github.com/apple-fritter/weechat.whois-aggregator): Aggregate whois data in a rolling CSV file. (Python)
- [weechat.youtube-info](https://github.com/apple-fritter/weechat.youtube-info): Extract video information from a YouTube URL and post it back to the channel. (Python)

### IRCcloud
- [irccloud-to-weechat](https://github.com/apple-fritter/irccloud-to-weechat): Convert IRC logs from IRCcloud format to Weechat format. (Rust)
- [irccloud-to-xchat](https://github.com/apple-fritter/irccloud-to-xchat): Convert IRC logs from IRCcloud format to XChat format. (Rust)

### X-Chat
- [xchat.channel-moderation](https://github.com/apple-fritter/xchat.channel-moderation): Moderate an IRC channel. (Python)
- [doppelganger](https://github.com/apple-fritter/doppelganger): X-Chat mIRC imposter. Fingerprint subversion. (Python bundle)

### Other
- [driftwood](https://github.com/apple-fritter/driftwood): A unified IRC log format definition. (Rust)

## [Disclaimer](DISCLAIMER)
**This software is provided "as is" and without warranty of any kind**, express or implied, including but not limited to the warranties of merchantability, fitness for a particular purpose and noninfringement. In no event shall the authors or copyright holders be liable for any claim, damages or other liability, whether in an action of contract, tort or otherwise, arising from, out of or in connection with the software or the use or other dealings in the software.

**The authors do not endorse or support any harmful or malicious activities** that may be carried out with the software. It is the user's responsibility to ensure that their use of the software complies with all applicable laws and regulations.

## License

These files released under the [MIT License](LICENSE).
