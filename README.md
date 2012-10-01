# Pseudo SMTP #

Simple SMTP end point.  This will listen for incoming SMTP sessions and record the results into a DB. This doesn't actually forward or deliver email in any sense, aside from saving it locally in a DB.

## What? ##

Automated testing of email sucks. There are a lot of projects out there intended to make testing email sending easier, but none fit the use case I needed, and so here we are.

This server requires no configuration with the exception of telling it what port to run on. By default it runs on port 8888. Any mail sent to it will be saved, irrelevant of the destination.

## Getting Started ##

 * Note that this server listens to incoming requests, but it does NOT provide a way to send outbound emails. If you want to have it send stuff, make sure you have a outgoing mail server such as Postfix installed and running.

1.  Take a look at config.py.
    1.  Redefine smtp\_server\_domain to either localhost or your domain name.
    2.  Redefine anything else you care to redefine.
2.  Run sh run\_smtp.sh

## Current Development Status ##

Currently the only addition is the ability to capture mail going to any address, and logs it if debug is enabled. The next step will be to save what's received into a db.

Running the server still requires running the run\_smtp.sh shell script. I want to make this a proper python script that will handling running the server in a more resilient manner, as well as improve logging.

## TODO ##
* Add saving of mail to db.
    * Add support for saving attachments.
* Tweak action\_mailboxes and pass\_through options.
    * Add config option to enable/disable.
* Add config value to enable/disable saving of mail to db.
* Tweak address validation to reflect RFCs 2822, 5322 and 6531.
* Add better logging.
* Enhance error results. Currently server only replies with 250 on success on 550 No such user on any error.

## Credits ##
This is a fork of the [intelligent smtp responder](https://github.com/dpapathanasiou/intelligent-smtp-responder).

## License ##
Licensed under MIT. See LICENSE.

