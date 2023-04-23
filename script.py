import weechat
import os
import csv
import datetime

weechat.register("whois_to_csv", "Author Name", "1.0", "MIT", "Save whois data to a rolling CSV file", "", "")

def whois_cb(data, buffer, args):
    server = weechat.buffer_get_string(buffer, "localvar_server")
    nick = args.split()[0]
    whois_info = weechat.info_get("irc_nick_info", "{0},{1}".format(server, nick))

    if whois_info:
        fields = [
            "nick",
            "username",
            "host",
            "realname",
        ]
        values = [nick]
        for field in fields[1:]:
            value = weechat.info_get("irc_nick_%s" % field, whois_info)
            values.append(value)

        filename = os.path.expanduser("~/weechat_whois.csv")
        file_exists = os.path.exists(filename)
        with open(filename, "a") as f:
            writer = csv.writer(f)
            if not file_exists:
                writer.writerow(fields)
            writer.writerow(values)

    return weechat.WEECHAT_RC_OK

weechat.hook_command("whois_to_csv", "Save whois data to a rolling CSV file", "[nick]", "", "", "whois_cb", "")
