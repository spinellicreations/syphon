syphon	
---------------------------------------------------------------------
# ... cause i'm just sittin out here readin barcodes,
#      take off and fly.  i'm tryin to figure out which
#      one you might be on, and why you don't love me
#      anymore.  ya i'm just sittin out here readin barcodes...
---------------------------------------------------------------------
# ... syphon is a telnet capture utility.  it is specifically
#     designed to read a 'line at a time' from devices such as
#     barcode readers or scales, which will output a EOL terminated
#     string upon event occurance.  
#
# ... syphon functions over ethernet, relying upon 'serial over eth'
#     devices, which are becoming more and more comon.  syphon 
#     will auto-reconnect at a specified interval if no data is
#     gathered, ensuring that you have reliability after events such
#     as device failure / power loss / etc.
#
# ... serial over eth devices should be setup as telnet servers, for
#     example - such devices which bear the 'Moxa' brand name should
#     be set to "TCP Server Mode".
---------------------------------------------------------------------
# ... syphon is based on blips.  that is to say that blips was a
#     proof of concept, proving that 'it could be done', but was
#     also very limited and had absolutely no fault recovery.
#     syphon seeks to perform all the functions of blips, but with
#     automated fault recovery and much greater speed / efficiency.
---------------------------------------------------------------------
#...  portions of syphon utilize implemtations published (free) by
#     Doug Hellmann (www.doughellmann.com), specifically with
#     regard to COMM.
---------------------------------------------------------------------
COPYRIGHT

# THE FOLLOWING 10 LINES MAY NOT BE REMOVED, but may be
#   appended with additional contributor info.
syphon Copyright (C) 2008-2012
V. Spinelli for Sorrento Lactalis American Group
This program comes with ABSOLUTELY NO WARRANTY;
As this program is based on [and has dependancies]
the content of GPL and LGPL works, GPL is preserved.
This is open software, released under GNU GPL v3,
and you are welcome to redistribute it, with this
tag in tact.
... http://www.sorrentolactalis.com/
... http://www.spinellicreations.com/
A copy of the GPL should be included with this work.
If you did not receive a copy, see...
http://www.gnu.org/licenses/gpl-3.0.txt
---------------------------------------------------------------------
---------------------------------------------------------------------
CONTACT		
		Author			V. Spinelli
				Email:	Vince@SpinelliCreations.com
				Site:	http://spinellicreations.com
				Handle:	PoweredByDodgeV8

		Copyright Holder	Sorrento Lactalis American Group
				Email:	http://www.sorrentocheese.com/about/contact.html
				Site:	http://www.sorrentolactalis.com
---------------------------------------------------------------------
README...
---------------------------------------------------------------------
---------------------------------------------------------------------
	OPC functionality requires you have already installed
	mod_openopc_2.

	REQUIREMENTS...
	---------------

	1- Python version 2.5 or greater (http://python.org)
	
	2- py-setproctitle library version 1.0 or greater (http://pypi.python.org/pypi/setproctitle)

	3- Linux (Preferred) / Unix / BSD / Windows ... whatever ...

	OPTIONAL (depends on what you want to use syphon for)...
	--------------------------------------------------------

	o-1- mod_openopc version 3.0.14 or greater (http://download.spinellicreations.com)
		-- only required if you want to push via OPC functionality, and this is external anyway

	o-2- MySQL-Python version 1.2 or greater (http://mysql-python.sourceforge.net)
		-- if you want to use the 'RUN_SEER_CHECKWEIGHERMODEL_V1' function
			-- this custom subroutine is written to integrate with the S.E.E.R.
			   CheckWeigher Model (v1-Eudamidas)

	
	BASIC USAGE...
	--------------
	
	/path/to/python /opt/syphon/prog/syphon.py [ARGS]
	
	ARGUMENTS...
	------------
	
	syphon.py RUN_OPC [preset_file] [LOG | NOLOG] [CONDITIONAL | NOTCONDITIONAL]
	-- -- Connect to the device indicated by the preset_file,
	-- -- and sit on the connection to receive data.  Upon
	-- -- receipt, export data to mod_openopc for immediate
	-- -- writing to the OPC device indicated by the preset_file.
	-- -- If logging is enabled, export data to mysql database, 
	-- -- with datestamp and data source identification.

	syphon.py RUN_MATCH [preset_file] [SEARCH | (blank)] [LOG | NOLOG]  [CONDITIONAL | NOTCONDITIONAL]
	-- -- Connect to the device indicated by the preset file,
	-- -- and sit on the connection to receive data.  Upon
	-- -- receipt, compare the data to a pre-declared value, and
	-- -- if it is a match, then export a declared value to 
	-- -- mod_openopc for immediate writing to the OPC device
	-- -- indicated by the preset_file.
	-- -- If logging is enabled, export data to mysql database, 
	-- -- with datestamp and data source identification.

	syphon.py RUN_CONDITIONAL_RESTRANSMIT [preset_file]
	-- -- Connect to the device indicated by the preset file,
	-- -- after a second client has connected to syphon.  Then,
	-- -- sit on the connection to recevive data.  Upon receipt,
	-- -- check for a database flag (value) to decide whether 
	-- -- we should retransmit the value to the second client,
	-- -- on the port indicated by the preset file.
	-- -- USES BLOCKING IO - only one secondary client per
	-- -- instance!

	syphon.py RUN_SEER_CHECKWEIGHERMODEL_V1 [preset_file]
	-- -- A -custom- subroutine written for integration with the
	-- -- S.E.E.R. CheckWeigher Model (v1-Eudamidas) which accepts
	-- -- scale data (weights), and logs them to a MySQL database
	-- -- along with the date / time, machine (preset) name, and
	-- -- the current running machine recipe (as indicated by the
	-- -- S.E.E.R. database table for CheckWeigher Model active
	-- -- syphon recipes).
	-- -- NOTE - this REQUIRES that you have already installed SEER
	-- -- -- and the CHECKWEIGHERMODEL, that you have created
	-- -- -- the appropriate SEER config files (global options and
	-- -- -- local options files), and that you have populated the
	-- -- -- 'SYPHON_table' prior to running this command in syphon

	syphon.py RUN_SEER_CHECKWEIGHERMODEL_V2 [preset_file]
	-- -- A -custom- subroutine written for integration with the
	-- -- S.E.E.R. CheckWeigher Model (v2-Leda) which functions
	-- -- precisely the same as the CHECKWEIGHERMODEL_V1 subroutine,
	-- -- with the added feature of logging the machine operator
	-- -- as well.

	syphon.py RUN_SEER_WARRIOR_EOR_ACQUIRE [preset_file]
	-- -- A -custom- subroutine written for integration with the
	-- -- S.E.E.R. Warrior Module's 'lactalis_bartender_labeling_system'
	-- -- plugin.
	-- -- Logs the last scanned barcode from a device by updating a field
	-- -- in a declared MySQL DB with the barcode value.
	-- -- NOTE - this REQUIRES that you have already installed SEER
	-- -- -- and the WARRIOR MODULE, that you have created
	-- -- -- the appropriate SEER config files (global options and
	-- -- -- local options files), installed and configured the
	-- -- -- proprietary 'lactalis_bartender_labeling_system' plugin,
	-- -- -- and populated tables for the plugin prior to running
	-- -- -- this command in syphon.

	syphon.py RUN_SEER_WARRIOR_EOR_EXECUTE [preset_file]
	-- -- A -custom- subroutine written for integration with the
	-- -- S.E.E.R. Warrior Module's 'lactalis_bartender_labeling_system'
	-- -- plugin.
	-- -- Scans a barcode from a device, compares it with a value stored
	-- -- by the EOR_ACQUIRE subroutine in a MySQL database, and upon
	-- -- finding a match, writes a declared value to a declared OPC
	-- -- target device.
	-- -- NOTE - this REQUIRES that you have already installed SEER
	-- -- -- and the WARRIOR MODULE, that you have created
	-- -- -- the appropriate SEER config files (global options and
	-- -- -- local options files), installed and configured the
	-- -- -- proprietary 'lactalis_bartender_labeling_system' plugin,
	-- -- -- and populated tables for the plugin prior to running
	-- -- -- this command in syphon.

	syphon.py RUN_MYSQL [preset_file] [CONDITIONAL | NOTCONDITIONAL]
	-- -- Connect to the device indicated by the preset_file
	-- -- and sit on the connection to receive data.  Upon
	-- -- receipt, export data to mysql database, with datestamp
	-- -- and data source identification.

	syphon.py TEST_COMM [device_ip_address] [device_port]
	      [EOL to search (optional)] [timeout (optional, 180]
	-- -- Connect to the device indicated by the arguments,
	-- -- but only accept the first input string.  This allows
	-- -- us to effectively test communication.

	syphon.py AUTO_LAUNCH CONFIRM
	-- -- auto launches all subroutines or syphon commands
	-- -- which are defined to auto launch in the global options
	-- -- file.
	-- -- this is a great command to use at system startup,
	-- -- rather than calling all of your presets individually.
	-- -- you should still test your individual presets first by
	-- -- running them individually, so you can observe their
	-- -- output in verbose mode... the auto launcher hides all
	-- -- output in the background.
	-- -- the CONFIRM argument is required, anything else
	-- -- will simply display a the items listed to auto launch
	-- -- along with the help-file, but not actually launch them.
	-- -- NOTE!
	-- -- -- Unix flavors should call AUTO_LAUNCH as follows...
	-- -- -- [path-to]/nohup [path-to]/python [path-to]syphon.py AUTO_LAUNCH CONFIRM 2>/dev/null 1>/dev/null &
	-- -- -- The above is recommend for use in your 'rc.local' or
	-- -- -- startup file.

	syphon.py HELP
	-- -- Brings you to the help screen.
	
	CONFIGURATION...
	----------------

	-- copy the source tree to /opt/syphon or c:\syphon\
	-- edit syphon/options/options.opt
		[global_runtime]
		FLAVOR:UNIX
		# operating system 
		# -- use UNIX for Linux, Unix, Solaris, BSD, etc, etc...
		# -- use WIN for Windows
		[global_path]
		PROGPATH_MODOPENOPC:/opt/mod_openopc_2
		# full path 
		# -- use c:\mod_openopc_2 for WIN
		# -- use /opt/mod_openopc_2 for UNIX
		PROGPATH_MODOPENOPC_GWCOMM:gwcomm
		# --------------------- COMMANDS ------------------------------------
		[global_commands]
		PYTHON_EXECUTABLE:/usr/local/bin/python
		# python executable
		# -- usually /usr/local/bin/python on UNIX
		# -- usually C:\Python\python.exe on WIN
		# --------------------- NETWORK CONNECTIONS -------------------------
		[global_network]
		MYIP:10.1.1.100				
		# what is your CU static IP address?
		MYDEFAULTGATEWAY:10.1.1.1			
		# what is your CU default gateway IP address?
		# ---------------------- AUTO LAUNCH --------------------------------
		[auto_launch]
		AUTO_LAUNCH:RUN_OPC,my_preset_1|RUN_OPC,mypreset_2|RUN_SEER_CHECKWEIGHERMODEL_V1,my_preset_3
		# define syphon routines to auto launch
		# -- form is COMMAND,preset-file-name,argument1,argument2,argument3|COMMAND,preset-file-name,argument1,argument2,argument3
		# -- DO NOT use any spaces. 
		# -- DO NOT use a trailing pipe. 
		# -- if a COMMAND does not have any arguments, then it would simply be...
		#       COMMAND,preset-file|COMMAND,preset-file,argument1|COMMAND,preset-file,argument1,argument2
		#	... you get the idea.
		#	... ultimately everything between 'pipes' is passed as a newly spawned process
		#	    where commas are replaced by whitespace.  So, the example above would be passed as...
		#		--> syphon.py COMMAND preset-file
		#		--> syphon.py COMMAND preset-file argument-1
		#		--> syphon.py COMMAND preset-file argument-1 argument-2
		# -------------------------------------------------------------------

		RUN_OPC PRESET FILES
		--------------------

		-- inside syphon/options/presets/, copy template.pre
		   and rename it as your first preset file.
		-- this type of preset MUST end in "[name].pre"
		-- preset file must include...

			[modopenopc]
			YOURMODOPENOPCDAEMON:grimlock_hmi			
			# mod_openopc write daemon being used
			YOURTARGET:[MOZZ_B_ELEVATOR]
			# mod_openopc OPC device topic name
			YOURLEAF:F8:0
			# mod_openopc target leaf to write to
			#
			[device]
			YOURDEVICEIP:10.1.12.110
			# target device IP address
			YOURDEVICEPORT:1028
			# target device telnet port
			YOURDEVICENAME:mozz_case_pack_b_scale
			# name this device, so it shows up
			# in your running processes
			YOURDEVICENAMEFORLOG:mozz_b_scale
			# what would you like the 'SOURCE' column to indicate in
			# the database record for values read from this device
			STARTCHAR:0
			# parse the data stream, start at...
			ENDCHAR:5
			# then end at...
			# NOTE - if you have a variable length incoming data, but
			#        always know your line will end with YOURENDOFLINE,
			#  	 then you can 'cheat' by setting ENDCHAR equal to
			#        some very high or ridiculous number, like 1000
			#        or 99
			REQUIRENUMERICVALUE:yes
			# do you want to require that only a
			# numeric value can be processed?
			# will prevent errors if accidently
			# trying to write a string to a numeric
			# plc register.
			# -- valid values are 'yes' or 'no'
			YOURENDOFLINE:\r\n\r
			# character or group of characters to
			# indicate the end of an input stream
			YOURTIMEOUT:300
			# data receive timeout, if no data
			# received in X seconds, then recycle
			# the connection.
			#
			[mysql]
			#
			# -- THE FOLLOWING ONLY REQUIRED IF OPTION "LOG" BEING USED ! --
			#
			MYSQLDB:mod_openopc		
			# DATABASE NAME
			MYSQLIP:127.0.0.1
			# IPADDRESS, should be "localhost" or actual IP address
			# -- USE "QUOTES" FOR IF RUNNING THIS PROGRAM UNDER UNIX
			# -- DO NOT USE QUOTES IF RUNNING UNDER WIN
			TABLE_SYPHON:SYPHON_MYSQL
			# MYSQL TABLE THAT HOLDS ALL GATHERED DATA,
			# THIS IS WHERE YOU WANT TO STORE THE DATA THAT SYPHON GATHERS
			# COLUMN 1 = DATESTAMP
			# COLUMN 2 = SOURCE
			# COLUMN 3 = VALUE
			MYSQLUSER:mysql		
			# YOUR MYSQL USERNAME
			MYSQLPASS:mysqlpassword
			# YOUR MYSQL PASSWORD
			COMMITTRANSACTIONS:YES
			# COMMIT DATABASE TRANSACTIONS AFTER EXECUTION
			# -- YES or NO
			# -- TRANSACTIONAL DATABASES SUCH AS INNODB REQUIRE
			#    THIS FUNCTIONALITY, FUTURE MYISAM WILL ALSO
			#
			# NOTE THE RETENTION TIME OF RECORDS IS SOMETHING
			#   YOU'LL HAVE TO 'FUDGE' IN SEER+mod_openopc
			#   OR ON YOUR OWN WITH YOUR OWN CUSTOM SCRIPT,
			#   AS WE CAN'T CARRY THAT FUNCTION OUT FROM HERE.
			#   FOR SEER+mod_openopc, JUST SET UP A 'preset' 
			#   SIMILAR TO THE SYSTEM_FAULTS ONE AND ENTER 
			#   YOUR RETENTION TIME.  WE ASSUME YOU HAVE A 
			#   FULL WORKING KNOWLEDGE OF mod_openopc.
			#
			# -- THE FOLLOWING ONLY REQUIRED IF OPTION "CONDITIONAL" BEING USED ! --
			#
			YOURDEVICETABLENAME:mydevicetablename
			# MYSQL TABLE A RECORD NAMED "YOURDEVICENAMEFORLOG" AND HAS
			# A VALUE ASSOCIATED WITH IT WHICH YOU WANT TO CONDITIONALLY CHECK AGAINST.
			# WE ASSUME THIS TABLE TO BE IN DATABASE "MYSQLDB".
			YOURDEVICECOLUMNNAME:mydevicecolumnname
			# NAME OF COLUMN WITHIN "YOURDEVICETABLENAME" THAT IDENTIFIES RECORDS
			# BY NAME DECLARED IN "YOURDEVICENAMEFORLOG"
			# -- NOTE -- if "YOURDEVICENAMEFORLOG" VARIABLE NOT PRESENT, SYPHON WILL USE
			# VARIABLE "YOURDEVICENAME" IN ITS PLACE!
			YOURCONDITIONALVALUE:myconditionalvalue
			# VALUE YOU WISH TO TEST AGAINST... IF WE SEE THIS VALUE IN NEXT COLUMN OF
			# "YOURDEVICETABLENAME", FOR RECORD IDENTIFIED AS "YOURDEVICENAMEFORLOG", THEN
			# WE WILL PROCEED WITH THE OPERATION, ELSE WE WILL SKIP IT.

		RUN_MATCH PRESET FILES
		-----------------------

		-- inside syphon/options/presets/, copy template.match
		   and rename it as your first preset file.
		-- this type of preset MUST end in "[name].match"
		-- preset file must include...

			[modopenopc]
			YOURMODOPENOPCDAEMON:grimlock_hmi			
			# mod_openopc write daemon being used
			YOURTARGET:[MOZZ_B_ELEVATOR]
			# mod_openopc OPC device topic name
			YOURLEAF:F8:0
			# mod_openopc target leaf to write to
			YOUREXECUTIONVALUE:1
			# value to write to target leaf upon successful match
			YOURMATCHVALUE:something_to_match
			# string you wish to test for a match against
			#
			[device]
			YOURDEVICEIP:10.1.12.110
			# target device IP address
			YOURDEVICEPORT:1028
			# target device telnet port
			YOURDEVICENAME:mozz_case_pack_b_scale
			# name this device, so it shows up
			# in your running processes
			YOURDEVICENAMEFORLOG:mozz_b_scale
			# what would you like the 'SOURCE' column to indicate in
			# the database record for values read from this device
			STARTCHAR:0
			# parse the data stream, start at...
			ENDCHAR:5
			# then end at...
			# NOTE - if you have a variable length incoming data, but
			#        always know your line will end with YOURENDOFLINE,
			#  	 then you can 'cheat' by setting ENDCHAR equal to
			#        some very high or ridiculous number, like 1000
			#        or 99
			REQUIRENUMERICVALUE:yes
			# do you want to require that only a
			# numeric value can be processed?
			# will prevent errors if accidently
			# trying to write a string to a numeric
			# plc register.
			# -- valid values are 'yes' or 'no'
			YOURENDOFLINE:\r\n\r
			# character or group of characters to
			# indicate the end of an input stream
			YOURTIMEOUT:300
			# data receive timeout, if no data
			# received in X seconds, then recycle
			# the connection.
			#
			[mysql]
			#
			# -- THE FOLLOWING ONLY REQUIRED IF OPTION "LOG" BEING USED ! --
			#
			MYSQLDB:mod_openopc		
			# DATABASE NAME
			MYSQLIP:127.0.0.1
			# IPADDRESS, should be "localhost" or actual IP address
			# -- USE "QUOTES" FOR IF RUNNING THIS PROGRAM UNDER UNIX
			# -- DO NOT USE QUOTES IF RUNNING UNDER WIN
			TABLE_SYPHON:SYPHON_MYSQL
			# MYSQL TABLE THAT HOLDS ALL GATHERED DATA,
			# THIS IS WHERE YOU WANT TO STORE THE DATA THAT SYPHON GATHERS
			# COLUMN 1 = DATESTAMP
			# COLUMN 2 = SOURCE
			# COLUMN 3 = VALUE
			MYSQLUSER:mysql		
			# YOUR MYSQL USERNAME
			MYSQLPASS:mysqlpassword
			# YOUR MYSQL PASSWORD
			COMMITTRANSACTIONS:YES
			# COMMIT DATABASE TRANSACTIONS AFTER EXECUTION
			# -- YES or NO
			# -- TRANSACTIONAL DATABASES SUCH AS INNODB REQUIRE
			#    THIS FUNCTIONALITY, FUTURE MYISAM WILL ALSO
			#
			# NOTE THE RETENTION TIME OF RECORDS IS SOMETHING
			#   YOU'LL HAVE TO 'FUDGE' IN SEER+mod_openopc
			#   OR ON YOUR OWN WITH YOUR OWN CUSTOM SCRIPT,
			#   AS WE CAN'T CARRY THAT FUNCTION OUT FROM HERE.
			#   FOR SEER+mod_openopc, JUST SET UP A 'preset' 
			#   SIMILAR TO THE SYSTEM_FAULTS ONE AND ENTER 
			#   YOUR RETENTION TIME.  WE ASSUME YOU HAVE A 
			#   FULL WORKING KNOWLEDGE OF mod_openopc.
			#
			# -- THE FOLLOWING ONLY REQUIRED IF OPTION "CONDITIONAL" BEING USED ! --
			#
			YOURDEVICETABLENAME:mydevicetablename
			# MYSQL TABLE A RECORD NAMED "YOURDEVICENAMEFORLOG" AND HAS
			# A VALUE ASSOCIATED WITH IT WHICH YOU WANT TO CONDITIONALLY CHECK AGAINST.
			# WE ASSUME THIS TABLE TO BE IN DATABASE "MYSQLDB".
			YOURDEVICECOLUMNNAME:mydevicecolumnname
			# NAME OF COLUMN WITHIN "YOURDEVICETABLENAME" THAT IDENTIFIES RECORDS
			# BY NAME DECLARED IN "YOURDEVICENAMEFORLOG"
			# -- NOTE -- if "YOURDEVICENAMEFORLOG" VARIABLE NOT PRESENT, SYPHON WILL USE
			# VARIABLE "YOURDEVICENAME" IN ITS PLACE!
			YOURCONDITIONALVALUE:myconditionalvalue
			# VALUE YOU WISH TO TEST AGAINST... IF WE SEE THIS VALUE IN NEXT COLUMN OF
			# "YOURDEVICETABLENAME", FOR RECORD IDENTIFIED AS "YOURDEVICENAMEFORLOG", THEN
			# WE WILL PROCEED WITH THE OPERATION, ELSE WE WILL SKIP IT.
			# -------------------------------------------------------------------

		RUN_MYSQL PRESET FILES
		----------------------

		-- inside syphon/options/presets/, copy template.mysql
		   and rename it as your first preset file.
		-- this type of preset MUST end in "[name].mysql"
		-- preset file must include...

			[device]
			YOURDEVICEIP:10.20.248.110
			# target device IP address
			YOURDEVICEPORT:1028
			# target device telnet port
			YOURDEVICENAME:mozz_case_pack_b_scale
			# name this device, so it shows up
			# in your running processes
			YOURDEVICENAMEFORLOG:mozz_b_scale
			# what would you like the 'SOURCE' column to indicate in
			# the database record for values read from this device
			STARTCHAR:0
			# parse the data stream, start at...
			ENDCHAR:5
			# then end at...
			# NOTE - if you have a variable length incoming data, but
			#        always know your line will end with YOURENDOFLINE,
			#  	 then you can 'cheat' by setting ENDCHAR equal to
			#        some very high or ridiculous number, like 1000
			#        or 99
			REQUIRENUMERICVALUE:yes
			# do you want to require that only a
			# numeric value can be processed?
			# -- valid values are 'yes' or 'no'
			YOURENDOFLINE:\r\n\r
			# character or group of characters to
			# indicate the end of an input stream
			YOURTIMEOUT:300
			# data receive timeout, if no data
			# received in X seconds, then recycle
			# the connection.
			#
			[mysql]
			MYSQLDB:mod_openopc		
			# DATABASE NAME
			MYSQLIP:127.0.0.1
			# IPADDRESS, should be "localhost" or actual IP address
			# -- USE "QUOTES" FOR IF RUNNING THIS PROGRAM UNDER UNIX
			# -- DO NOT USE QUOTES IF RUNNING UNDER WIN
			TABLE_SYPHON:SYPHON_MYSQL
			# MYSQL TABLE THAT HOLDS ALL GATHERED DATA,
			# THIS IS WHERE YOU WANT TO STORE THE DATA THAT SYPHON GATHERS
			# COLUMN 1 = DATESTAMP
			# COLUMN 2 = SOURCE
			# COLUMN 3 = VALUE
			MYSQLUSER:mysql		
			# YOUR MYSQL USERNAME
			MYSQLPASS:mysqlpassword
			# YOUR MYSQL PASSWORD
			COMMITTRANSACTIONS:YES
			# COMMIT DATABASE TRANSACTIONS AFTER EXECUTION
			# -- YES or NO
			# -- TRANSACTIONAL DATABASES SUCH AS INNODB REQUIRE
			#    THIS FUNCTIONALITY, FUTURE MYISAM WILL ALSO
			#
			# NOTE THE RETENTION TIME OF RECORDS IS SOMETHING
			#   YOU'LL HAVE TO 'FUDGE' IN SEER+mod_openopc
			#   OR ON YOUR OWN WITH YOUR OWN CUSTOM SCRIPT,
			#   AS WE CAN'T CARRY THAT FUNCTION OUT FROM HERE.
			#   FOR SEER+mod_openopc, JUST SET UP A 'preset' 
			#   SIMILAR TO THE SYSTEM_FAULTS ONE AND ENTER 
			#   YOUR RETENTION TIME.  WE ASSUME YOU HAVE A 
			#   FULL WORKING KNOWLEDGE OF mod_openopc.
			#
			# -- THE FOLLOWING ONLY REQUIRED IF OPTION "CONDITIONAL" BEING USED ! --
			#
			YOURDEVICETABLENAME:mydevicetablename
			# MYSQL TABLE A RECORD NAMED "YOURDEVICENAMEFORLOG" AND HAS
			# A VALUE ASSOCIATED WITH IT WHICH YOU WANT TO CONDITIONALLY CHECK AGAINST.
			# WE ASSUME THIS TABLE TO BE IN DATABASE "MYSQLDB".
			YOURDEVICECOLUMNNAME:mydevicecolumnname
			# NAME OF COLUMN WITHIN "YOURDEVICETABLENAME" THAT IDENTIFIES RECORDS
			# BY NAME DECLARED IN "YOURDEVICENAMEFORLOG"
			YOURCONDITIONALVALUE:myconditionalvalue
			# VALUE YOU WISH TO TEST AGAINST... IF WE SEE THIS VALUE IN NEXT COLUMN OF
			# "YOURDEVICETABLENAME", FOR RECORD IDENTIFIED AS "YOURDEVICENAMEFORLOG", THEN
			# WE WILL PROCEED WITH THE OPERATION, ELSE WE WILL SKIP IT.
			# -------------------------------------------------------------------

		RUN_SEER_CHECKWEIGHERMODEL_V1 PRESET FILES
		------------------------------------------

		-- inside syphon/options/presets/, copy template.seer_cw
		   and rename it as your first preset file.
		-- this type of preset MUST end in "[name].seer_cw"

		-- NOTE -- it is assumed that you have a strong understanding of both SEER,
			   and mod_openopc if using this function.  syphon will not 'clean'
			   your database; we expect you to use the DB Maint features within
			   mod_openopc by simply creating a 'fake' preset file within 
			   mod_openopc (similar to the 'system_faults' one - actually identical),
			   and allowing that to be your cleaning-function... which will also
			   regulate record retention, as the mod_openopc database preset 
			   indicates the retention time for all tables within the database.
			   Here is an example -->

				# -------------------------------------------------------------------
				# mod_openopc -- syphon_checkweighermodel_v1.pre
				# -------------------------------------------------------------------
				# ... integrating the Python OpenOPC project to run HMI
				#     over Linux, BSD, Unix in an unfettered manner.
				# -------------------------------------------------------------------
				# -------------------------------------------------------------------
				# COPYRIGHT
				#
				# SEE README FILE FOR COPYRIGHT INFORMATION
				# -------------------------------------------------------------------
				# -------------------------------------------------------------------
				#
				# --------------------- QUICK INFO ----------------------------------
				# THIS IS A PRESET TEMPLATE FOR ---READING--- ONLY.
				# REPEAT! THIS IS FOR READING OPC DATA INTO SQL TABLES ONLY!
				# --------------------- DECLARATIONS --------------------------------
				#
				[your_server]
				YOUROPCSERVER:none
				# preset opc server name
				YOURSQLSERVER:mod_openopc		
				# preset sql server name
				YOURSQLTABLE:CHECKWEIGHERMODEL			
				# preset sql table
				COMMENTENABLE:no
				# 'yes' or 'no', if yes, then set
				#  below to presetname_comment, or name
				#  of table holding the comments.
				#  if no, set below to 'none'
				YOURSQLCOMMENTTABLE:none
				# preset sql table
				# correspondes to comments for this preset.
				# comment column counts as a filler column,
				# so do NOT include a comment column as
				# part of the sqlcolumncount, rather, count
				# it as part of the fillercount.
				YOURSQLFILLERCOUNT:0
				# integer number, corresponding to the 
				# number of empty cells of columns left
				# at the right hand side of your table.
				# this is useful for inserting partial 
				# records.  set to 0 if you're not
				# using it, or if your leafers will
				# fill up entire row in table.
				YOURSQLCOLUMNCOUNT:0
				#
				[your_read]
				YOURLEAFERS:none
				#	preset leaves to read, follow form LEAFIDENTIFICATION&|
				#	where & delineates columns in the table and | delineates rows
				#	TYPICALLY, LEAFS ARE IN THE FORM OF ...
				#		[TARGETNAME]TAG
				#	SUCH AS...
				#		[MY_PLC]N7:42
				#
				# -------------------------------------------------------------------

			You can then run the cleanup / old record delete from the command line
			or schedule it as a job via existing mod_openopc db cleanup routines.

		-- syphon preset file must include...

			[mysql]
			MYSQLDB:mod_openopc		
			# DATABASE NAME
			MYSQLIP:localhost
			# IPADDRESS, should be "localhost" or actual IP address
			# -- USE "QUOTES" FOR IF RUNNING THIS PROGRAM UNDER UNIX
			# -- DO NOT USE QUOTES IF RUNNING UNDER WIN
			CHECKWEIGHERMODEL_TABLE_SYPHON:CHECKWEIGHERMODEL_SYPHON
			# MYSQL TABLE THAT HOLDS ASSOCIATIONS OF MACHINENAME TO ACTIVE
			# RUNNING RECIPE WHERE MACHINENAME IS COLUMN 1, AND RECIPE IS 
			# COLUMN 2
			# -- FOR VERSION 2 ONLY, OPERATOR NAME UNIQUE ID IS COLUMN 3
			CHECKWEIGHERMODEL_TABLE:CHECKWEIGHERMODEL
			# MYSQL TABLE THAT HOLDS ALL CHECKWEIGHER GATHERED DATA,
			# THIS IS WHERE YOU WANT TO STORE THE DATA THAT SYPHON GATHERS
			MYSQLUSER:mysql		
			# YOUR MYSQL USERNAME
			MYSQLPASS:mysqlpassword
			# YOUR MYSQL PASSWORD
			COMMITTRANSACTIONS:YES
			# COMMIT DATABASE TRANSACTIONS AFTER EXECUTION
			# -- YES or NO
			# -- TRANSACTIONAL DATABASES SUCH AS INNODB REQUIRE
			#    THIS FUNCTIONALITY, FUTURE MYISAM WILL ALSO
			#
			# NOTE THE RETENTION TIME OF RECORDS IS SOMETHING
			#   YOU'LL HAVE TO 'FUDGE' IN SEER+mod_openopc
			#   AS WE CAN'T CARRY THAT FUNCTION OUT FROM HERE
			#   JUST SET UP A 'preset' SIMILAR TO THE SYSTEM_FAULTS
			#   ONE AND ENTER YOUR RETENTION TIME.  WE ASSUME
			#   YOU HAVE A FULL WORKING KNOWLEDGE OF mod_openopc.
			# 
			[device]
			YOURDEVICEIP:10.1.1.101
			# target device IP address
			YOURDEVICEPORT:1026
			# target device telnet port
			YOURDEVICENAME:my_checkweigher_2
			# name this device, so it shows up
			# in your running processes
			YOURDEVICENAMEFORLOG:MY_CHECKWEIGHER_2
			# what is the name you gave this device in SEER 
			# localoptions file under the identification...
			#      "$CHECKWEIGHERMODEL_NAME[{int}]=YOURDEVICENAMEFORLOG"
			STARTCHAR:0
			# parse the data stream, start at...
			ENDCHAR:6
			# then end at...
			# NOTE - if you have a variable length incoming data, but
			#        always know your line will end with YOURENDOFLINE,
			#  	 then you can 'cheat' by setting ENDCHAR equal to
			#        some very high or ridiculous number, like 1000
			#        or 99
			REQUIRENUMERICVALUE:yes
			# do you want to require that only a
			# numeric value can be processed?
			# will prevent errors if accidently
			# trying to write a string to a numeric
			# plc register.
			# -- valid values are 'yes' or 'no'
			YOURENDOFLINE:.\r\n
			# character or group of characters to
			# indicate the end of an input stream
			YOURSCALEFACTOR:0.0352739619
			# if you need to convert from one unit of measure
			# to another, then enter your scale factor here...
			# for example, to convert from grams to ounces,
			# simply enter a scale factor of 0.0352739619
			YOURTIMEOUT:300
			# data receive timeout, if no data
			# received in X seconds, then recycle
			# the connection.

		RUN_SEER_CHECKWEIGHERMODEL_V2 PRESET FILES
		------------------------------------------

		-- see the section for CHECKWEIGHERMODEL_V1 preset files, as these
		   are identical.

		RUN_SEER_WARRIOR_EOR_ACQUIRE PRESET FILES
		-----------------------------------------

		-- inside syphon/options/presets/, copy template.war_eor_aq
		   and rename it as your first preset file.
		-- this type of preset MUST end in "[name].war_eor_aq"
		-- preset file must include...
			[mysql]
			MYSQLDB:mod_openopc		
			# DATABASE NAME
			MYSQLIP:localhost
			# IPADDRESS, should be "localhost" or actual IP address
			# -- USE "QUOTES" FOR IF RUNNING THIS PROGRAM UNDER UNIX
			# -- DO NOT USE QUOTES IF RUNNING UNDER WIN
			EOR_TABLE:BARTENDER_END_OF_RUN
			# MYSQL TABLE THAT HOLDS ASSOCIATIONS OF MACHINENAME TO END
			# OF RUN DATA...  
			# COLUMN 1 = LINE # 
			# COLUMN 2 = EOR (ACTUAL)
			# COLUMN 3 = EOR PENDING
			# COLUMN 4 = DATESTAMP OF EOR UPDATE (ACTUAL)
			# COLUMN 5 = OPERATOR
			MYSQLUSER:mysql		
			# YOUR MYSQL USERNAME
			MYSQLPASS:mysqlpassword
			# YOUR MYSQL PASSWORD
			COMMITTRANSACTIONS:YES
			# COMMIT DATABASE TRANSACTIONS AFTER EXECUTION
			# -- YES or NO
			# -- TRANSACTIONAL DATABASES SUCH AS INNODB REQUIRE
			#    THIS FUNCTIONALITY, FUTURE MYISAM WILL ALSO
			# 
			[device]
			YOURDEVICEIP:10.1.1.99
			# target device IP address
			YOURDEVICEPORT:4001
			# target device telnet port
			YOURDEVICENAME:my_labls_scanner_1
			# name this device, so it shows up
			# in your running processes
			YOURDEVICENAMEFORLOG:LABLSSCAN1
			# what is the name you gave this device in WARRIOR LaBLS
			# plugin options file under the identification... 
			#	"$bartender_LINE_ID_BY_NUMBER[{int}][{int}]=YOURDEVICENAMEFORLOG"
			#	NOTE - this does not have to be a string... it can be a number
			#	if that is how you are declaring your lines (by number).
			STARTCHAR:0
			# parse the data stream, start at...
			ENDCHAR:6
			# then end at...
			# NOTE - if you have a variable length incoming data, but
			#        always know your line will end with YOURENDOFLINE,
			#  	 then you can 'cheat' by setting ENDCHAR equal to
			#        some very high or ridiculous number, like 1000
			#        or 99
			REQUIRENUMERICVALUE:yes
			# do you want to require that only a
			# numeric value can be processed?
			# will prevent errors if accidently
			# trying to write a string to a numeric
			# plc register.
			# -- valid values are 'yes' or 'no'
			YOURENDOFLINE:\r\n
			# character or group of characters to
			# indicate the end of an input stream
			YOURTIMEOUT:300
			# data receive timeout, if no data
			# received in X seconds, then recycle
			# the connection.

		RUN_SEER_WARRIOR_EOR_EXECUTE PRESET FILES
		-----------------------------------------

		-- inside syphon/options/presets/, copy template.war_eor_ex
		   and rename it as your first preset file.
		-- this type of preset MUST end in "[name].war_eor_ex"
		-- preset file must include...
			[mysql]
			MYSQLDB:mod_openopc		
			# DATABASE NAME
			MYSQLIP:localhost
			# IPADDRESS, should be "localhost" or actual IP address
			# -- USE "QUOTES" FOR IF RUNNING THIS PROGRAM UNDER UNIX
			# -- DO NOT USE QUOTES IF RUNNING UNDER WIN
			EOR_TABLE:BARTENDER_END_OF_RUN
			# MYSQL TABLE THAT HOLDS ASSOCIATIONS OF MACHINENAME TO END
			# OF RUN DATA...  
			# COLUMN 1 = LINE # 
			# COLUMN 2 = EOR (ACTUAL)
			# COLUMN 3 = EOR PENDING
			# COLUMN 4 = DATESTAMP OF EOR UPDATE (ACTUAL)
			# COLUMN 5 = OPERATOR
			MYSQLUSER:mysql		
			# YOUR MYSQL USERNAME
			MYSQLPASS:mysqlpassword
			# YOUR MYSQL PASSWORD
			COMMITTRANSACTIONS:YES
			# COMMIT DATABASE TRANSACTIONS AFTER EXECUTION
			# -- YES or NO
			# -- TRANSACTIONAL DATABASES SUCH AS INNODB REQUIRE
			#    THIS FUNCTIONALITY, FUTURE MYISAM WILL ALSO
			# 
			[device]
			YOURDEVICEIP:10.1.1.99
			# target device IP address
			YOURDEVICEPORT:4001
			# target device telnet port
			YOURDEVICENAME:my_labls_scanner_1
			# name this device, so it shows up
			# in your running processes
			YOURDEVICENAMEFORLOG:LABLSSCAN1
			# what is the name you gave this device in WARRIOR LaBLS
			# plugin options file under the identification... 
			#	"$bartender_LINE_ID_BY_NUMBER[{int}][{int}]=YOURDEVICENAMEFORLOG"
			#	NOTE - this does not have to be a string... it can be a number
			#	if that is how you are declaring your lines (by number).
			STARTCHAR:0
			# parse the data stream, start at...
			ENDCHAR:6
			# then end at...
			# NOTE - if you have a variable length incoming data, but
			#        always know your line will end with YOURENDOFLINE,
			#  	 then you can 'cheat' by setting ENDCHAR equal to
			#        some very high or ridiculous number, like 1000
			#        or 99
			REQUIRENUMERICVALUE:yes
			# do you want to require that only a
			# numeric value can be processed?
			# will prevent errors if accidently
			# trying to write a string to a numeric
			# plc register.
			# -- valid values are 'yes' or 'no'
			YOURENDOFLINE:\r\n
			# character or group of characters to
			# indicate the end of an input stream
			YOURTIMEOUT:300
			# data receive timeout, if no data
			# received in X seconds, then recycle
			# the connection.
			#
			[modopenopc]
			YOURMODOPENOPCDAEMON:grimlock_hmi			
			# mod_openopc write daemon being used
			YOURTARGET:[MOZZ_B_ELEVATOR]
			# mod_openopc OPC device topic name
			YOURLEAF:F8:0
			# mod_openopc target leaf to write to
			YOUREXECUTIONVALUE:1
			# value to write to target leaf upon successful match
---------------------------------------------------------------------
