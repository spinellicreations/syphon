#!/usr/bin/python
# -------------------------------------------------------------------
# syphon -- options.py
# -------------------------------------------------------------------
# ... glomming your telnet data since 2009.
# -------------------------------------------------------------------
# --------------------- IMPORT FUNCTIONS ----------------------------
import pdb			# the python debugger, because noone
				#    is perfect.  enable its use by
				#    placing the following tag where
				#    you would like to begin line by
				#    line hashing...
				#      pdb.set_trace()
#pdb.set_trace()		# uncomment to debug entire program
import gc			# python garbage collector
import sys			# basic
import ConfigParser		# enables us to use presets
import telnetlib		# enables us to speak to serial io
				#    over telnet
import time			# we need a clock
from datetime import datetime	# we need date and time stamps
import shutil			# lets us move files around
import os			# allos us to run native system
				#    commands from within python
import subprocess		# allow forking
import threading		# launch threads for subroutines and
				#    or to run cycles
import socket			# telnet broadcast comm
import random			# sane event file creation
try:
	import setproctitle	# identify running processes
except:
	pass
# -------------------------------------------------------------------
# COPYRIGHT
#
# THE FOLLOWING 10 LINES MAY NOT BE REMOVED, but may be
#   appended with additional contributor info.
print ""
print "------------------------------------------------------------"
print "------------------------------------------------------------"
print "syphon Copyright (C) 2008-2013"  
print "V. Spinelli for Sorrento Lactalis American Group"
print "------------------------------------------------------------"
print "This program comes with ABSOLUTELY NO WARRANTY;"
print "As this program is based on [and has dependancies]"
print "the content of GPL and LGPL works, GPL is preserved."
print ""
print "This is open software, released under GNU GPL v3,"
print "and you are welcome to redistribute it, with this"
print "tag in tact."
print "... http://www.sorrentolactalis.com/"
print "... http://www.spinellicreations.com/"
print ""
print "A copy of the GPL should be included with this work."
print "If you did not receive a copy, see..."
print "http://www.gnu.org/licenses/gpl-3.0.txt"
print "------------------------------------------------------------"
print "-- The only people who have anything to fear from"
print "-- free software are those whose products are worth"
print "-- even less. - David Emery"
print "------------------------------------------------------------"
print "version number = 0.1-11 (build #27)"
print "------------------------------------------------------------"
print "------------------------------------------------------------"
print ""
# -------------------------------------------------------------------
# -------------------------------------------------------------------
#
# --------------------- ENABLE GARBAGE COLLECTOR --------------------
gc.enable()
#
# --------------------- FUNCTION DEFINITION -------------------------
config = ConfigParser.ConfigParser()
#
# --------------------- GLOBAL OPTIONS ------------------------------
# THE GLOBAL PRESET FILE
# -- WHAT IS CURRENT WORKING DIRECTORY
global_presetpath = sys.path[0]
# -- HARD CODE REFERENCE TO OPTIONS FOLDER AND THE GLOBAL OPTIONS FILE
# -- -- TO DO SO, REMOVE '/prog' FROM THE PATH DECLARATION
global_hardcodedroot = global_presetpath[:-5]
global_presetpath = os.path.join(global_hardcodedroot, 'options', 'options.opt')
global_presetpath = os.path.normpath(global_presetpath)

# -- AGNOSTIC PRESET FILE
# -- -- PRE-DETERMINE PRESET FILE BASED UPON mod_openopc BUILTIN SNIFFER
# -- -- THIS SHOULD WORK FOR ALL POSIX AND WIN OS.
global_presetfile = open(global_presetpath,"r")
	#	the global_presetfile must be edited by the user and hardcoded
	#	so that all other directories will fall into line
try:
	print ""
	print "NOTICE! -- YOUR PATHS ARE AUTO-DEFINED"
	print "AS FOLLOWS..."
	PROGPATH = global_hardcodedroot
	print "-- PROGPATH= " + PROGPATH
	PROGPATH_OPTIONS = "options"
	PROGPATH_OPTIONS = os.path.join(PROGPATH, PROGPATH_OPTIONS)
	print "-- PROGPATH_OPTIONS= " + PROGPATH_OPTIONS
	PROGPATH_PRE = "presets"
	PROGPATH_PRE = os.path.join(PROGPATH_OPTIONS, PROGPATH_PRE)
	print "-- PROGPATH_PRE= " + PROGPATH_PRE
	PROGPATH_PROG = "prog"
	PROGPATH_PROG = os.path.join(PROGPATH, PROGPATH_PROG)
	print "-- PROGPATH_PROG= " + PROGPATH_PROG
	SYPHON_EXECUTABLE = os.path.join(PROGPATH_PROG, "syphon.py")		
	TEMPDIR = "temp"
	TEMPDIR = os.path.join(PROGPATH, TEMPDIR)
	print "-- TEMPDIR= " + TEMPDIR
	# ADD SECTIONS FROM GLOBAL PRESET FILE
	config.add_section("global_path")
	config.add_section("global_options")
	config.add_section("global_commands")
	config.add_section("global_network")
	config.add_section("auto_launch")
	# READ FROM THE GLOBAL PRESET FILE
	config.readfp(global_presetfile)
	# ASSIGN VARS BASED ON THE GLOBAL PRESET FILE
	# -- PATHS
	print ""
	print "NOTICE! -- YOUR 3rd PARTY PATHS ARE DEFINED IN THE GLOBAL"
	print "OPTIONS FILE AS FOLLOWS..."
	PROGPATH_MODOPENOPC = config.get("global_path","PROGPATH_MODOPENOPC")	
	print "-- PROGPATH_MODOPENOPC= " + PROGPATH_MODOPENOPC
	PROGPATH_MODOPENOPC_GWCOMM = config.get("global_path","PROGPATH_MODOPENOPC_GWCOMM")
	PROGPATH_MODOPENOPC_GWCOMM = os.path.join(PROGPATH_MODOPENOPC, PROGPATH_MODOPENOPC_GWCOMM)
	print "-- PROGPATH_MODOPENOPC_GWCOMM= " + PROGPATH_MODOPENOPC_GWCOMM
	# -- SYSTEM COMMANDS
	PYTHON_EXECUTABLE = config.get("global_commands","PYTHON_EXECUTABLE")
	# -- NETWORK CONNECTIONS
	print ""
	print "NOTICE! -- YOUR NETWORK IS DEFINED IN THE GLOBAL"
	print "OPTIONS FILE AS FOLLOWS..."
	MYIP = config.get("global_network","MYIP")
	print "-- YOUR IP ADDRESS= " + MYIP
	MYDEFAULTGATEWAY = config.get("global_network","MYDEFAULTGATEWAY")
	print "-- YOUR GATEWAY= " + MYDEFAULTGATEWAY
	# -- OPTIONS
	print ""
	print "NOTICE! -- YOUR OPTIONS ARE DEFINED IN THE GLOBAL"
	print "OPTIONS FILE AS FOLLOWS..."
	EXPORT_9999_ON_NON_NUMERIC = config.get("global_options","EXPORT_9999_ON_NON_NUMERIC")
	print "-- EXPORT_9999_ON_NON_NUMERIC= " + EXPORT_9999_ON_NON_NUMERIC
	# -- AUTO LAUNCHER
	AUTO_LAUNCH = config.get("auto_launch","AUTO_LAUNCH")
	AUTO_LAUNCH = AUTO_LAUNCH.split('|')
	#
	OK_GLOBAL_OPTS = '1'
	global_presetfile.close()
except:
	OK_GLOBAL_OPTS = '0'
	global_presetfile.close()
#
# PN ------------------ BEGIN ERROR DEFINITION --------------- END PN
# -- ERROR - A HEADER FOR ALL ERROR FUNCTIONS
def syphon_error_all_header():
	print ""
	print "ERROR!"
# -- ERROR - A FOOTER FOR ALL ERROR FUNCTIONS
def syphon_error_all_footer():
	print ""
	print "This window will automatically close (or the routine will"
	print "quit) in 30 seconds." 
	time.sleep(30)
# -- ERROR CANNOT CONNECT TO SQL DATABASE
def syphon_error_sql():
	syphon_error_all_header()
	print "We were unable to connect to your selected MySQL database."
	print "Perhaps you have setup incorrect options in..."
	print "-- options/presets/YOURPRESET.[ext]"
	print "Or your SQL server may be down, either way, you must correct"
	print "this before you can proceed."
	syphon_error_all_footer()
# -- ERROR CANNOT PROPERLY CLOSE SQL DATABASE
def syphon_error_sql_close():
	# DECLARE GLOBAL VARS
	global sql_connect, sql_cursor
	syphon_error_all_header()
	print "Failed to close MySQL connection gracefully."
	sql_connect = ''
	sql_cursor = ''
	# RETURN ARGS
	return sql_connect, sql_cursor
# -- ERROR OPTIONS FILES NOT PROPERLY IMPORTED OR BAD
def syphon_error_options():
	syphon_error_all_header()
	print "Something is wrong with the syntax or entries within one of"
	print "your options files or preset files..."
	print "-- options/presets/[preset].pre"
	print "Please correct this before trying to run this routine again."
	syphon_error_all_footer()
# -- ERROR AUTO LAUNCHER HAS FAILED OR FAULTED
def syphon_error_autolaunch():
	syphon_error_all_header()
	print "We were unable to connect to execute the AUTO_LAUNCH request."
	print "Perhaps you have mistyped the names of your presets in the"
	print "global options file?  Or perhaps you've malformed the AUTO_LAUNCH"
	print "variable string?"
	print "... elsewise, something is seriously fragged, or you may be using"
	print "an older version of Python which does not support all of the"
	print "functions necessary for this task."
	syphon_error_all_footer()
# -- ERROR COMMAND REQUESTED BUT YOU DID NOT SUPPLY ALL ARGUMENTS NEEDED
def syphon_error_command():
	# DECLARE GLOBAL VARS
	global YOURCOMMAND1
	syphon_error_all_header()
	print "You've chosen to run the..."
	print YOURCOMMAND1
	print "...routine, however, you have not supplied us with all"
	print "of the required arguments to do so.  Please run HELP"
	print "to learn more."
	syphon_error_all_footer()
# -- ERROR IN GLOBAL OPTIONS FILE OR MAYBE BAD PERMISSIONS
def syphon_error_global_options():
	syphon_error_all_header()
	print "Your GLOBAL OPTIONS file is not loading properly.  Either"
	print "the syntax is bad or the text of your option arguments are."
	print "Please read the README file and refer to the default options"
	print "file under..."
	print "-- options/default_options.opt"
	syphon_error_all_footer()
# -- ERROR IN COMMUNICATION UPON INITIAL STARTUP
def syphon_error_communication():
	syphon_error_all_header()
	print "Can't connect to your target device, perhaps it is not"
	print "powered on?  Please check it out and try again."
	syphon_error_all_footer()
# PN ------------------ END ERROR DEFINITION ----------------- END PN
#
# PN ------------------ BEGIN OK_GLOBAL_OPTS CONDITIONAL ----- END PN
if OK_GLOBAL_OPTS == '1':
#
# --------------------- CLI ARGUMENTS -------------------------------
# COMMAND ARGUMENTS ASSUME THIS PROGRAM TO BE ARGUMENT ZERO
	# -- VARS
	OK_RUN_OPC = 0
	OK_RUN_MATCH = 0
	OK_RUN_CONDITIONAL_RETRANSMIT = 0
	OK_RUN_SEER_CHECKWEIGHERMODEL_V1 = 0
	OK_RUN_SEER_CHECKWEIGHERMODEL_V2 = 0
	OK_RUN_SEER_WARRIOR_EOR_ACQUIRE = 0
	OK_RUN_SEER_WARRIOR_EOR_EXECUTE = 0
	OK_RUN_MYSQL = 0
	OK_TEST_COMM = 0
	OK_AUTO_LAUNCH = 0
#
	try:
		YOURCOMMAND1 = sys.argv[1]
		if YOURCOMMAND1 == '-h':
			YOURCOMMAND1 = "HELP"
		else:
			if YOURCOMMAND1 == '--help':
				YOURCOMMAND1 = "HELP"
			else:
				YOURCOMMAND1 = YOURCOMMAND1
	except:
		YOURCOMMAND1 = "HELP"
	try:
		YOURCOMMAND2 = sys.argv[2]
	except:
		YOURCOMMAND2 = "null"
	try:
		YOUROPTION1 = sys.argv[2]
		OK_RUN_OPC = OK_RUN_OPC + 1
		OK_RUN_MATCH = OK_RUN_MATCH + 1
		OK_RUN_CONDITIONAL_RETRANSMIT = OK_RUN_CONDITIONAL_RETRANSMIT + 1
		OK_RUN_SEER_CHECKWEIGHERMODEL_V1 = OK_RUN_SEER_CHECKWEIGHERMODEL_V1 + 1
		OK_RUN_SEER_CHECKWEIGHERMODEL_V2 = OK_RUN_SEER_CHECKWEIGHERMODEL_V2 + 1
		OK_RUN_SEER_WARRIOR_EOR_ACQUIRE = OK_RUN_SEER_WARRIOR_EOR_ACQUIRE + 1
		OK_RUN_SEER_WARRIOR_EOR_EXECUTE = OK_RUN_SEER_WARRIOR_EOR_EXECUTE + 1
		OK_RUN_MYSQL = OK_RUN_MYSQL + 1
		OK_TEST_COMM = OK_TEST_COMM + 1
		OK_AUTO_LAUNCH = OK_AUTO_LAUNCH + 1
	except:
		YOUROPTION1 = "null"
		OK_RUN_OPC = OK_RUN_OPC - 1
		OK_RUN_MATCH = OK_RUN_MATCH - 1
		OK_RUN_CONDITIONAL_RETRANSMIT = OK_RUN_CONDITIONAL_RETRANSMIT - 1
		OK_RUN_SEER_CHECKWEIGHERMODEL_V1 = OK_RUN_SEER_CHECKWEIGHERMODEL_V1 - 1
		OK_RUN_SEER_CHECKWEIGHERMODEL_V2 = OK_RUN_SEER_CHECKWEIGHERMODEL_V2 - 1
		OK_RUN_SEER_WARRIOR_EOR_ACQUIRE = OK_RUN_SEER_WARRIOR_EOR_ACQUIRE - 1
		OK_RUN_SEER_WARRIOR_EOR_EXECUTE = OK_RUN_SEER_WARRIOR_EOR_EXECUTE - 1
		OK_RUN_MYSQL = OK_RUN_MYSQL - 1
		OK_TEST_COMM = OK_TEST_COMM - 1
		OK_AUTO_LAUNCH = OK_AUTO_LAUNCH - 1
	try:
		YOUROPTION2 = sys.argv[3]
		OK_RUN_OPC = OK_RUN_OPC + 1
		OK_RUN_MATCH = OK_RUN_MATCH + 1
		OK_TEST_COMM = OK_TEST_COMM + 1
	except:
		YOUROPTION2 = "null"
		OK_RUN_OPC = OK_RUN_OPC - 1
		OK_RUN_MATCH = OK_RUN_MATCH - 1
		OK_TEST_COMM = OK_TEST_COMM - 1
	try:
		YOUROPTION3 = sys.argv[4]
	except:
		YOUROPTION3 = "null"
	try:
		YOUROPTION4 = sys.argv[5]
	except:
		YOUROPTION4 = "null"
	try:
		YOUROPTION5 = sys.argv[6]
	except:
		YOUROPTION5 = "null"
#
# --------------------- DEFINITIONS ---------------------------------
	# PULL IN PRESETS
	# -- PRESET FILE
	def pull_in_preset():
		# DECLARE GLOBAL VARS
		global mysql_is_down, YOURCONDITIONALVALUE, YOURMATCHWAIT, YOURDEVICETABLENAME, YOURDEVICECOLUMNNAME, YOURBROADCASTPORT, REQUIRE_MYSQL, YOURMATCHVALUE, YOURSCALEFACTOR, YOURDEVICENAMEFORLOG, SQL_DB, SQL_IP, SQL_USER, SQL_PASS, COMMITTRANSACTIONS, EOR_TABLE, ACTION_TABLE, TABLE_SYPHON, YOUREXECUTIONVALUE, CHECKWEIGHERMODEL_TABLE_SYPHON, CHECKWEIGHERMODEL_TABLE, YOURCOMMAND1, YOURMODOPENOPCDAEMON, YOURDEVICEIP, YOURDEVICEPORT, YOURDEVICENAME, STARTCHAR, ENDCHAR, YOURTARGET, YOURLEAF, YOURTIMEOUT, YOURTIMEOUT_INT, YOURENDOFLINE, REQUIRENUMERICVALUE
		# PULL PRESET OPTIONS
		pre_presetfile = os.path.join(PROGPATH_PRE, YOUROPTION1)
		if (YOURCOMMAND1 == 'RUN_OPC'):
			pre_presetfile = pre_presetfile + ".pre"
			# DO WE NEED MYSQL INTERACTIVITY ?
			if (YOUROPTION2 == 'LOG'):
				REQUIRE_MYSQL = 1
			else:
				REQUIRE_MYSQL = 0
			# IS THIS A SPECIAL JOB ?
			SPECIAL_JOB = 0
		else:
			if (YOURCOMMAND1 == 'RUN_MATCH'):
				pre_presetfile = pre_presetfile + ".match"
				# DO WE NEED MYSQL INTERACTIVITY ?
				if (YOUROPTION3 == 'LOG'):
					REQUIRE_MYSQL = 1
				else:
					REQUIRE_MYSQL = 0
				# IS THIS A SPECIAL JOB ?
				SPECIAL_JOB = 0
			else:
				if (YOURCOMMAND1 == 'RUN_CONDITIONAL_RETRANSMIT'):
					pre_presetfile = pre_presetfile + ".cond_retrans"
					# DO WE NEED MYSQL INTERACTIVITY ?
					REQUIRE_MYSQL = 1
					# IS THIS A SPECIAL JOB ?
					SPECIAL_JOB = 0
				else:
					if (YOURCOMMAND1 == 'RUN_MYSQL'):
						pre_presetfile = pre_presetfile + ".mysql"
						# DO WE NEED MYSQL INTERACTIVITY ?
						REQUIRE_MYSQL = 1
						# IS THIS A SPECIAL JOB ?
						SPECIAL_JOB = 0
					else:
						if (YOURCOMMAND1 == 'RUN_SEER_CHECKWEIGHERMODEL_V1') or (YOURCOMMAND1 == 'RUN_SEER_CHECKWEIGHERMODEL_V2'):
							pre_presetfile = pre_presetfile + ".seer_cw"
							# DO WE NEED MYSQL INTERACTIVITY ?
							REQUIRE_MYSQL = 1
							# IS THIS A SPECIAL JOB ?
							SPECIAL_JOB = 1
						else:
							if (YOURCOMMAND1 == 'RUN_SEER_WARRIOR_EOR_ACQUIRE'):
								pre_presetfile = pre_presetfile + ".war_eor_aq"
								# DO WE NEED MYSQL INTERACTIVITY ?
								REQUIRE_MYSQL = 1
								# IS THIS A SPECIAL JOB ?
								SPECIAL_JOB = 1
							else:
								if (YOURCOMMAND1 == 'RUN_SEER_WARRIOR_EOR_EXECUTE'):
									pre_presetfile = pre_presetfile + ".war_eor_ex"
									# DO WE NEED MYSQL INTERACTIVITY ?
									REQUIRE_MYSQL = 1
									# IS THIS A SPECIAL JOB ?
									SPECIAL_JOB = 1
								else:
									# MISBEHAVING COMMANDS DEFAULT TO THE 'pre' FILE EXTENSION
									# THIS IS NON-IDEAL BEHAVIOR, BUT WE WILL ALLOW IT FOR THE LAZY
									# PROGRAMMERS OR THOSE WHO NEED TO DEBUG
									pre_presetfile = pre_presetfile + ".pre"
									# DO WE NEED MYSQL INTERACTIVITY ?
									REQUIRE_MYSQL = 0
		print ""
		print "NOTICE! -- YOUR PRE_PRESETFILE IS..."
		print pre_presetfile
		pre_presetfile = open(pre_presetfile,"r")
		print "-- opened."
		#
		# CONDITIONALLY LOAD SECTION 'mod_openopc'
		if (YOURCOMMAND1 == 'RUN_OPC') or (YOURCOMMAND1 == 'RUN_SEER_WARRIOR_EOR_EXECUTE'):
			config.add_section("modopenopc")
			print "-- -- added section 'modopenopc'."
		else:
			pass
		# CONDITIONALLY LOAD SECTION 'broadcast'
		if (YOURCOMMAND1 == 'RUN_CONDITIONAL_RETRANSMIT'):
			config.add_section("broadcast")
			print "-- -- added section 'broadcast'."
		else:
			pass
		# CONDITIONALLY LOAD SECTION 'mysql'
		if (REQUIRE_MYSQL == 1):
			config.add_section("mysql")
			print "-- -- added section 'mysql'."
		else:
			pass
		# ALWAYS LOAD SECTION 'device'
		config.add_section("device")
		print "-- -- added section 'device'."
		#
		# -- READ FROM THE RUN PRESET FILE
		config.readfp(pre_presetfile)
		print "-- reading."
		# -- ASSUME FOLLOWING VARS ARE NULL UNLESS EXPLICITLY DECLARED
		YOURMODOPENOPCDAEMON = 'null'
		YOURTARGET = 'null'
		YOURLEAF = 'null'
		YOURMATCHVALUE = 'null'
		YOURMATCHWAIT = 'null'
		YOURSCALEFACTOR = 'null'
		YOUREXECUTIONVALUE = 'null'
		YOURBROADCASTPORT = 'null'
		YOURDEVICETABLENAME = 'null'
		YOURDEVICECOLUMNNAME = 'null'
		YOURCONDITIONALVALUE = 'null'
		# -- ASSIGN VARS BASED ON THE RUN PRESET FILE
		if YOURCOMMAND1 == 'RUN_OPC':
			YOURMODOPENOPCDAEMON = config.get("modopenopc","YOURMODOPENOPCDAEMON")
			print "-- -- your mod_openopc daemon = " + YOURMODOPENOPCDAEMON
			YOURTARGET = config.get("modopenopc","YOURTARGET")
			print "-- -- your mod_openopc target = " + YOURTARGET
			YOURLEAF = config.get("modopenopc","YOURLEAF")
			print "-- -- your mod_openopc leaf = " + YOURLEAF
			if YOUROPTION3 == 'CONDITIONAL':
				YOURDEVICETABLENAME = config.get("mysql","YOURDEVICETABLENAME")
				print "-- -- your device table name (to look for conditional check) = " + YOURDEVICETABLENAME
				YOURDEVICECOLUMNNAME = config.get("mysql","YOURDEVICECOLUMNNAME")
				print "-- -- your device column name (to look for conditional check) = " + YOURDEVICECOLUMNNAME
				YOURCONDITIONALVALUE = config.get("mysql","YOURCONDITIONALVALUE")
				print "-- -- your match value to run conditonal check against = " + YOURCONDITIONALVALUE
			else:
				pass
		else:
			if YOURCOMMAND1 == 'RUN_MATCH':
				YOURMODOPENOPCDAEMON = config.get("modopenopc","YOURMODOPENOPCDAEMON")
				print "-- -- your mod_openopc daemon = " + YOURMODOPENOPCDAEMON
				YOURTARGET = config.get("modopenopc","YOURTARGET")
				print "-- -- your mod_openopc target = " + YOURTARGET
				YOURLEAF = config.get("modopenopc","YOURLEAF")
				print "-- -- your mod_openopc leaf = " + YOURLEAF
				YOUREXECUTIONVALUE = config.get("modopenopc","YOUREXECUTIONVALUE")
				YOUREXECUTIONVALUE = str(YOUREXECUTIONVALUE)
				print "-- -- your mod_openopc execution value = " + YOUREXECUTIONVALUE
				YOURMATCHVALUE = config.get("modopenopc","YOURMATCHVALUE")
				YOURMATCHVALUE = str(YOURMATCHVALUE)
				print "-- -- your mod_openopc match value = " + YOURMATCHVALUE
				if YOUROPTION4 == 'CONDITIONAL':
					YOURDEVICETABLENAME = config.get("mysql","YOURDEVICETABLENAME")
					print "-- -- your device table name (to look for conditional check) = " + YOURDEVICETABLENAME
					YOURDEVICECOLUMNNAME = config.get("mysql","YOURDEVICECOLUMNNAME")
					print "-- -- your device column name (to look for conditional check) = " + YOURDEVICECOLUMNNAME
					YOURCONDITIONALVALUE = config.get("mysql","YOURCONDITIONALVALUE")
					print "-- -- your match value to run conditonal check against = " + YOURCONDITIONALVALUE
				else:
					pass
			else:
				if YOURCOMMAND1 == 'RUN_CONDITIONAL_RETRANSMIT':
					YOURDEVICECOLUMNNAME = config.get("mysql","YOURDEVICECOLUMNNAME")
					print "-- -- your device column name (to look inside of) = " + YOURDEVICECOLUMNNAME
					YOURBROADCASTPORT = config.get("broadcast","YOURBROADCASTPORT")
					print "-- -- your retransmission broadcast port = " + YOURBROADCASTPORT
					YOURMATCHVALUE = config.get("broadcast","YOURMATCHVALUE")
					print "-- -- your match value to check against = " + YOURMATCHVALUE
					YOURMATCHWAIT = config.get("broadcast","YOURMATCHWAIT")
					print "-- -- your match value to check against = " + YOURMATCHWAIT
					YOURMATCHVALUE = str(YOURMATCHVALUE)
				else:
					if (YOURCOMMAND1 == 'RUN_SEER_CHECKWEIGHERMODEL_V1') or (YOURCOMMAND1 == 'RUN_SEER_CHECKWEIGHERMODEL_V2'):
						CHECKWEIGHERMODEL_TABLE_SYPHON = config.get("mysql","CHECKWEIGHERMODEL_TABLE_SYPHON")
						print "-- -- your mysql checkweighermodel syphon table = " + CHECKWEIGHERMODEL_TABLE_SYPHON
						CHECKWEIGHERMODEL_TABLE = config.get("mysql","CHECKWEIGHERMODEL_TABLE")
						print "-- -- your mysql checkweighermodel table = " + CHECKWEIGHERMODEL_TABLE
						YOURSCALEFACTOR = config.get("device","YOURSCALEFACTOR")
						print "-- -- your scale factor (for incoming data) = " + YOURSCALEFACTOR
						# ZERO OUT THE UNUSED ONES - THIS IS A SPECIAL JOB
						EOR_TABLE = 'null'
						ACTION_TABLE = 'null'
					else:
						if YOURCOMMAND1 == 'RUN_SEER_WARRIOR_EOR_ACQUIRE':
							EOR_TABLE = config.get("mysql","EOR_TABLE")
							print "-- -- your mysql warrior EOR table = " + EOR_TABLE
							# ZERO OUT THE UNUSED ONES - THIS IS A SPECIAL JOB
							CHECKWEIGHERMODEL_TABLE_SYPHON = 'null'
							CHECKWEIGHERMODEL_TABLE = 'null'
							ACTION_TABLE = 'null'
						else:
							if YOURCOMMAND1 == 'RUN_SEER_WARRIOR_EOR_EXECUTE':
								EOR_TABLE = config.get("mysql","EOR_TABLE")
								print "-- -- your mysql warrior EOR table = " + EOR_TABLE
								ACTION_TABLE = config.get("mysql","ACTION_TABLE")
								print "-- -- your mysql warrior ACTION table = " + ACTION_TABLE
								YOURMODOPENOPCDAEMON = config.get("modopenopc","YOURMODOPENOPCDAEMON")
								print "-- -- your mod_openopc daemon = " + YOURMODOPENOPCDAEMON
								YOURTARGET = config.get("modopenopc","YOURTARGET")
								print "-- -- your mod_openopc target = " + YOURTARGET
								YOURLEAF = config.get("modopenopc","YOURLEAF")
								print "-- -- your mod_openopc leaf = " + YOURLEAF
								YOUREXECUTIONVALUE = config.get("modopenopc","YOUREXECUTIONVALUE")
								YOUREXECUTIONVALUE = str(YOUREXECUTIONVALUE)
								print "-- -- your mod_openopc execution value = " + YOUREXECUTIONVALUE
								# ZERO OUT THE UNUSED ONES - THIS IS A SPECIAL JOB
								CHECKWEIGHERMODEL_TABLE_SYPHON = 'null'
								CHECKWEIGHERMODEL_TABLE = 'null'
							else:
								if (YOURCOMMAND1 == 'RUN_MYSQL'):
									if YOUROPTION2 == 'CONDITIONAL':
										YOURDEVICETABLENAME = config.get("mysql","YOURDEVICETABLENAME")
										print "-- -- your device table name (to look for conditional check) = " + YOURDEVICETABLENAME
										YOURDEVICECOLUMNNAME = config.get("mysql","YOURDEVICECOLUMNNAME")
										print "-- -- your device column name (to look for conditional check) = " + YOURDEVICECOLUMNNAME
										YOURCONDITIONALVALUE = config.get("mysql","YOURCONDITIONALVALUE")
										print "-- -- your match value to run conditonal check against = " + YOURCONDITIONALVALUE
									else:
										pass
								else:
									# SPANK THE LAZY PROGRAMMER BY NOT LOADING ANYTHING
									# WHICH SHOULD RESULT IN A PYTHON RUNTIME FAULT
									pass
		if (SPECIAL_JOB == 0):
			CHECKWEIGHERMODEL_TABLE_SYPHON = 'null'
			CHECKWEIGHERMODEL_TABLE = 'null'
			EOR_TABLE = 'null'
			ACTION_TABLE = 'null'
		else:
			pass
		YOURDEVICEIP = config.get("device","YOURDEVICEIP")
		print "-- -- your device ip address = " + YOURDEVICEIP
		YOURDEVICEPORT = config.get("device","YOURDEVICEPORT")
		print "-- -- your device port = " + YOURDEVICEPORT
		YOURDEVICENAME = config.get("device","YOURDEVICENAME")
		print "-- -- your device name = " + YOURDEVICENAME
		STARTCHAR = config.get("device","STARTCHAR")
		print "-- -- your start character = " + STARTCHAR
		STARTCHAR = int(STARTCHAR)
		ENDCHAR = config.get("device","ENDCHAR")
		print "-- -- your end character = " + ENDCHAR
		ENDCHAR = int(ENDCHAR)
		REQUIRENUMERICVALUE = config.get("device","REQUIRENUMERICVALUE")
		print "-- -- require a numeric value from device = " + REQUIRENUMERICVALUE
		YOURENDOFLINE = config.get("device","YOURENDOFLINE")
		print "-- -- your end of line characters are = " + YOURENDOFLINE
		YOURTIMEOUT = config.get("device","YOURTIMEOUT")
		print "-- -- your timeout = " + YOURTIMEOUT
		YOURTIMEOUT_INT = int(YOURTIMEOUT)
		if (REQUIRE_MYSQL == 1):
			SQL_DB = config.get("mysql","MYSQLDB")
			print "-- -- your mysql database = " + SQL_DB
			SQL_IP = config.get("mysql","MYSQLIP")
			print "-- -- your mysql ip address = " + SQL_IP
			SQL_USER = config.get("mysql","MYSQLUSER")
			print "-- -- your mysql user = " + SQL_USER
			SQL_PASS = config.get("mysql","MYSQLPASS")
			print "-- -- your mysql password = " + SQL_PASS
			COMMITTRANSACTIONS = config.get("mysql","COMMITTRANSACTIONS")
			print "-- -- are we commiting mysql transactions? = " + COMMITTRANSACTIONS
			if (SPECIAL_JOB == 1):
				TABLE_SYPHON = 'null'
			else:
				TABLE_SYPHON = config.get("mysql","TABLE_SYPHON")
				print "-- -- your mysql syphon table = " + TABLE_SYPHON
			try:
				YOURDEVICENAMEFORLOG = config.get("device","YOURDEVICENAMEFORLOG")
				print "-- -- your device name (for log) = " + YOURDEVICENAMEFORLOG
			except:
				YOURDEVICENAMEFORLOG = YOURDEVICENAME
		else:
			# ZERO OUT THE UNUSED ONES
			SQL_DB = 'null'
			SQL_IP = 'null'
			SQL_USER = 'null'
			SQL_PASS = 'null'
			COMMITTRANSACTIONS = 'null'
			TABLE_SYPHON = 'null'
			YOURDEVICENAMEFORLOG = 'null'
		# RETURN THE VARS
		mysql_is_down = 0
		return mysql_is_down, YOURCONDITIONALVALUE, YOURMATCHWAIT, YOURDEVICETABLENAME, YOURDEVICECOLUMNNAME, YOURBROADCASTPORT, REQUIRE_MYSQL, YOURMATCHVALUE, YOURSCALEFACTOR, YOURDEVICENAMEFORLOG, SQL_DB, SQL_IP, SQL_USER, SQL_PASS, COMMITTRANSACTIONS, EOR_TABLE, ACTION_TABLE, YOUREXECUTIONVALUE, CHECKWEIGHERMODEL_TABLE_SYPHON, CHECKWEIGHERMODEL_TABLE, YOURMODOPENOPCDAEMON, YOURDEVICEIP, YOURDEVICEPORT, YOURDEVICENAME, STARTCHAR, ENDCHAR, YOURTARGET, YOURLEAF, YOURTIMEOUT, YOURENDOFLINE, YOURTIMEOUT_INT, REQUIRENUMERICVALUE
	# FIRE UP PRECURSOR SUBROUTINES
	# -- SQL CONNECT
	def fire_up_sql():
		# LOAD THE PYTHON MODULE
		import MySQLdb			# to speak to our database MySQL req'd
						# not MSSQL friendly
		# DECLARE GLOBAL VARS
		global REQUIRE_MYSQL, SQL_USER, SQL_PASS, SQL_DB, sql_connect, sql_cursor, SQL_IP
		if REQUIRE_MYSQL == 1:
			# SANITY CHECK - BECAUSE WE DO INSANE THINGS
			try:
				sql_cursor.close ()
				sql_connect.close ()
			except:
				pass
			sql_connect = MySQLdb.connect (host=SQL_IP, user=SQL_USER, passwd=SQL_PASS, db=SQL_DB)
			sql_cursor = sql_connect.cursor ()
		else:
			sql_connect = ''
			sql_cursor = ''
		# RETURN ARGS
		return sql_connect, sql_cursor
	# -- TELNET CONNECTION
	def fire_up_telnet():
		print ""
		print "INITIATING TELNET CONNECTION TO DEVICE."
		global YOURDEVICEIP, YOURDEVICEPORT, tn
		try:
			try:
				# SANITY CHECK, BECAUSE WE DO INSANE THINGS
				tn.close()
			except:
				pass
			tn = telnetlib.Telnet(YOURDEVICEIP, YOURDEVICEPORT)
			datestamp = datetime.now()
			datestamp = datestamp.strftime("%Y_%m%d_%H-%M-%S")
			print "CONNECTION SUCCESSFUL, WAITING ON INPUT... at " + datestamp
			print ""
			established = 1
		except:
			established = 0
			print "-- -- failed."
			print "-- -- trying agian..."
			time.sleep(3)
			while established == 0:
                                try:
                                        # -- TRY AGAIN
                                        tn = telnetlib.Telnet(YOURDEVICEIP, YOURDEVICEPORT)
                                        established = 1
                                except:
                                        print "-- -- failed."
                                        print "-- -- will try again in 60 seconds..."
                                        time.sleep(60)
                                        print ""
					datestamp = datetime.now()
					datestamp = datestamp.strftime("%Y_%m%d_%H-%M-%S")
                                        print "-- PERPETUAL CONNECT TRY at " + datestamp
			datestamp = datetime.now()
			datestamp = datestamp.strftime("%Y_%m%d_%H-%M-%S")
                        if established == 0:
                                # -- FAIL
                                print ""
                                print "FAULT FATAL!!!! -- HARD EXIT NEXT at " + datestamp
                                fault = "INITIAL_CONNECTION_COMM_TOTALFAILURE"
                                exit()
                        else:
                                # -- UN-FAIL
                                print ""
                                print "CONNECTION SUCCESSFUL, WAITING ON INPUT... at " + datestamp
				print ""
		return tn
	#	
	# -- FAULT - A HEADER FOR ALL FAULT FUNCTIONS
	def syphon_fault_all_header():
		print ""
		print "FAULT!"
	# -- FAULT RECYCLE
	# -- -- UPDATED AND REPLACES THE NOW DEPRECATED 'syphon_fault_unk()' UNKNOWN FAULT FUNCTION
	def syphon_fault_recycle():
		# DECLARE GLOBAL VARS
		global fault, REQUIRE_MYSQL
		print ""
		print fault
		# TRY TO HANDLE this FAULT INSTED OF DYING
		# -- CLOSE THE telnet CONNECTION
		datestamp = datetime.now()
		datestamp = datestamp.strftime("%Y_%m%d_%H-%M-%S")
		try:
			tn.close()
			print ""
			print "-- TELNET CONNECTION CLOSED at " + datestamp
			print ""
		except:
			print ""
			print "-- Failure to close connetion to Telnet Device,"
			print "hard drop will follow at " + datestamp
		# -- WAIT
		time.sleep(3)
		# -- RECONNECTING
		datestamp = datetime.now()
		datestamp = datestamp.strftime("%Y_%m%d_%H-%M-%S")
		print "-- 1st RECONN TRY at " + datestamp
		try:
			fire_up_telnet()
			restored = 1
		except:
			restored = 0
			print "-- -- failed."
			print ""
		while restored == 0:
			try:
				# -- TRY AGAIN
				print "-- -- trying again..."
				fire_up_telnet()
				restored = 1
			except:
				print "-- -- failed."
				print "-- -- will try again in 3 seconds..."
				print ""
				time.sleep(3)
		datestamp = datetime.now()
		datestamp = datestamp.strftime("%Y_%m%d_%H-%M-%S")
		if REQUIRE_MYSQL == 1:
			if restored == 1:
				# -- RECYCLE DATABASE CONNECTION AS WELL
				try:
					sql_cursor.close ()
					sql_connect.close ()
					print ""
					print "-- MySQL DB CONNECTION CLOSED at " + datestamp
					print ""
				except:
					syphon_error_sql_close()
					print ""
					print "-- Failure to close connetion to MySQL DB,"
					print "hard drop executed at " + datestamp
				# -- WAIT
				time.sleep(1)
				# -- RECONNECTING
				datestamp = datetime.now()
				datestamp = datestamp.strftime("%Y_%m%d_%H-%M-%S")
				print "-- MySQL DB RECONNECT ATTEMPT at " + datestamp
				try:	
					fire_up_sql()
					print "-- -- success!"
				except:
					restored == 0
					print "-- -- failed."
			else:
				pass
		else:
			pass
		if restored == 1:
			# -- UN-FAIL
			print ""
			print "DEVICE COMM RECYCLED!!! at " + datestamp
		else:
			# -- FAIL
			print ""
			print "FAULT FATAL!!!! -- HARD EXIT NEXT"
			fault = "RECYCLE_COMM_TOTALFAILURE at " + datestamp
			exit()
		print ""
		# -- RETURN
		return fault
	# -- FAULT UNKNOWN
	# -- -- DEPRECATED AND REPLACED BY 'syphon_fault_recycle()' DEVICE AND DB COMM
	# -- -- RE-ESTABLISHMENT FUNCTION
#
# --------------------- SUBROUTINES ---------------------------------
#
# RUN_OPC
	if YOURCOMMAND1 == 'RUN_OPC':
		print ""
		print "STARTING ROUTINE - RUN_OPC"
		if OK_RUN_OPC >= 2:
		# -- RUN_OPC
		# -- -- A ROUTINE TO READ TELNET DATE LINE BY LINE AND
		# -- -- THEN PUSH THAT DATA OUT TO A mod_openopc DAEMON
		# -- -- FOR WRITING TO A PLC OR OTHER DEVICE.
		# -- -- YOURCOMMAND1 	... RUN_OPC
		# -- -- YOUROPTION1	... PRESET FILE NAME wo EXTENSION
		# -- -- YOUROPTION2	... LOG | (blank)
		# -- -- YOUROPTION3	... CONDITIONAL | (blank)
			#
			# SCAN ALL PRESETS AND OPTIONS
			try:
				pull_in_preset()
				# DECLARE THAT WE HAVE ACHIEVED A GOOD PRESET AND OPTIONS PULL
				OK_PRE_OPT_PULL = 1
				# NAME THIS THREAD
				THREADNAME = "syphon_RUN_OPC_" + YOURDEVICENAME
				try:
					setproctitle.setproctitle(THREADNAME)	
				except:
					pass
			except:
				OK_PRE_OPT_PULL = 0
			#
			if OK_PRE_OPT_PULL == 1:
			# PN ------------------ BEGIN GUTS_OF_ROUTINE ------------------- END PN
				if (REQUIRE_MYSQL == 1):
					# CONNECT TO THE MySQL DATABASE
					try:
						# DEFINE WHAT IS USED AS A SPLITTER FOR MySQL PUSHES
						#   THIS IS ALWAYS A COMMA
						splitter = str(',')
						# INITIALIZE DATA DUMP HOLDING REGISTER
						value_final = ''
						fire_up_sql()
						mysql_is_down = 0
					except:
						mysql_is_down = 1
				else:
					pass
				# PROCEED ONLY IF THE MySQL SERVER CAN BE CONTACTED
				if ((mysql_is_down != 1) or (REQUIRE_MYSQL == 0)):
					# CONNECT TO THE TELNET DEVICE
					try:
						fire_up_telnet()
						telnet_is_down = 0
					except:
						telnet_is_down = 1
					# PROCEED ONLY IF THE DEVICE CAN BE CONTACTED
					while telnet_is_down != 1:
						try:	
							try:
								# -- READ EXPECT WITH A TIMEOUT
								RAWINPUT = tn.expect([YOURENDOFLINE],YOURTIMEOUT_INT)
								print "-- Value Incoming..."
								print " -- -- In RAW form..."
								print RAWINPUT
								INPUT1, INPUT2, INPUT3 = RAWINPUT
								print "-- -- In STRING form..."
								INPUT = str(RAWINPUT)
								INPUT1 = str(INPUT1)
								INPUT2 = str(INPUT2)
								INPUT3 = str(INPUT3)
								INPUT3 = INPUT3.replace(YOURENDOFLINE,'')
								print "-- -- -- INDEX: " + INPUT1
								print "-- -- -- MATCH: " + INPUT2
								print "-- -- -- VALUE: " + INPUT3
								if INPUT == 'EOFError':
									DROPPED = 1
									fault = "-- I/O miscommunication or Receive Error."
								else:
									if INPUT2 == 'None':
										DROPPED = 1
										fault = "-- Timeout, no data in " + YOURTIMEOUT + " seconds."
									else:
										DROPPED = 0
								CHECKING = 0
								if DROPPED == 0:
									CHECKING = 1
									INPUT_OUT = INPUT3[STARTCHAR:ENDCHAR]
									print "-- -- -- PARSED: " + INPUT_OUT
									print ""
									RECYCLE_COMM = 0
									# CHECK for NUMERIC VALUE
									if REQUIRENUMERICVALUE == 'yes':
										print "-- Checking for numeric data value..."
										try:
											TEST_NUMERIC = float(INPUT_OUT)
											print "-- -- data value IS numeric."
											print ""
											INPUT_OUT = float(INPUT_OUT)
											INPUT_OUT = str(INPUT_OUT)
										except:
											print "-- -- data value is NOT numeric."
											print "-- -- DISCARDING!"
											print ""
											if (EXPORT_9999_ON_NON_NUMERIC != 'YES'):
												DROPPED = 1
											else:
												print "-- -- -- exporting 9999 per option."
												INPUT_OUT = float(9999)
												INPUT_OUT = str(INPUT_OUT)
									else:
										print "-- Ignoring data type (string or numeric)..."
										print ""
									# PERFORM CONDITIONAL QUERY AND CHECK FOR CONDITIONAL MATCH
									if YOUROPTION3 == 'CONDITIONAL':
										print "-- Checking for condition required to handle data value..."
										trigger_query = "SELECT * FROM " + YOURDEVICETABLENAME + " WHERE " + YOURDEVICECOLUMNNAME + " LIKE \'" + YOURDEVICENAMEFORLOG + "\' ORDER BY DATESTAMP DESC LIMIT 1"
										trigger_query = str(trigger_query)
										print "-- -- Conditional value to test, incoming..."
			                                                        print trigger_query
										sql_cursor.execute (trigger_query)
										# COMMIT QUERY TO DB
										# -- PATCH FOR InnoDB ENGINE (and future MyISAM Engine)
										if COMMITTRANSACTIONS == "YES":
											try:
												# PUNCH THE CHANGE IN
												sql_connect.commit()
											except:
												# REVERT
												sql_connect.rollback()
										value_trigger = sql_cursor.fetchone()
										value_trigger = value_trigger[2]
										value_trigger = str(value_trigger)
			                                                        print value_trigger
										print "-- Checking for conditional match data value... (" + str(YOURCONDITIONALVALUE) + " =?= " + str(value_trigger) + ")"
										if str(YOURCONDITIONALVALUE) == str(value_trigger):
											print "-- -- match FOUND!"
											print ""
										else:
											print "-- -- match NOT found."
											print "-- -- DISCARDING!"
											print ""
											DROPPED = 1
								else:
									RECYCLE_COMM = 1
							except:
								INPUT_OUT = int(0)
								DROPPED = 1
								RECYCLE_COMM = 1
								fault = "-- Garbage Data Receive... Refreshing Connection."
							if DROPPED == 0:
								# IF INPUT IS NOT BAD THEN PUSH IT TO mod_openopc
								datestamp = datetime.now()
								datestamp = datestamp.strftime("%Y_%m%d_%H-%M-%S")
								FLATFILE = os.path.join(TEMPDIR, THREADNAME)
								FLATFILE = FLATFILE + "_" + datestamp + "_" + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + ".temp"
								print "-- built export file..."
								print FLATFILE
								FLATFILE_WORK = file(FLATFILE,'wt')
								FLATFILE_WORK = open(FLATFILE,'w')
								FLATFILE_CONTENT = "# START WRITE_DAEMON EVENT FILE FROM syphon.\n"
								FLATFILE_CONTENT = FLATFILE_CONTENT + "[your_write_type]\n"
								FLATFILE_CONTENT = FLATFILE_CONTENT + "YOURWRITETYPE:DECLARED\n"
								FLATFILE_CONTENT = FLATFILE_CONTENT + "# -- WRITE DECLARED VALUES TO OPC TARGET\n"
								FLATFILE_CONTENT = FLATFILE_CONTENT + "[your_leafers]\n"
								FLATFILE_CONTENT = FLATFILE_CONTENT + "YOURLEAFERS:"
								FLATFILE_CONTENT = FLATFILE_CONTENT + "XXX" + YOURTARGET + "YYY" + YOURLEAF + "&" + INPUT_OUT + "&|" + "\n"
								FLATFILE_CONTENT = FLATFILE_CONTENT + "YOURWRITEPRESET:NONE\n"
								FLATFILE_CONTENT = FLATFILE_CONTENT + "# -- NAME OF PRESET FILE TO WRITE\n"
								FLATFILE_CONTENT = FLATFILE_CONTENT + "# END OF FILE\n"
								FLATFILE_WORK.write(FLATFILE_CONTENT)
								FLATFILE_WORK.close()
								# MOVE THE TEMP FILE TO THE DAEMON IMPORT DIRECTORY
								EXPORT = os.path.join(PROGPATH_MODOPENOPC_GWCOMM, YOURMODOPENOPCDAEMON)
								EXPORT = os.path.join(EXPORT, THREADNAME)
								EXPORT = EXPORT + "_" + datestamp + "_" + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + ".event"
								shutil.move(FLATFILE,EXPORT)
								print "-- handed the file off to mod_openopc..."
							else:
								print "-- not exporting anything..."
							if ((RECYCLE_COMM == 0) and (CHECKING == 1)):
								if (YOUROPTION2 == 'LOG'):
									# IF INPUT IS NOT BAD THEN PUSH IT TO MySQL DATABASE TABLE
									datestamp = datetime.now()
									datestamp = datestamp.strftime("%Y_%m%d_%H:%M:%S")
									# ASSEMBLE THE FINAL VALUE FOR EXPORT (ALL FIELDS OF CHECKWEIGHER TABLE [DATA TABLE])
									value_final = "\'" + datestamp + "\'" + splitter + "\'" + YOURDEVICENAMEFORLOG + "\'" + splitter + "\'" + str(INPUT3) + "\'"
									# PUSH THE ROW INTO THE DATABASE
									# -- psuedo_query_example = INSERT INTO SQL_TABLE VALUES(value_final)
									sql_query = "INSERT INTO " + TABLE_SYPHON + " VALUES(" + value_final + ")"
									print ""
									print "NOTICE! -- EXPORTING RESULTS TO YOUR SQL TABLE - FOR..." + YOURDEVICENAMEFORLOG
									print "WE ARE USING THE FOLLOWING QUERY STRING..."
									print sql_query
									sql_query = str(sql_query)
									sql_cursor.execute (sql_query)
									# COMMIT QUERY TO DB
									# -- PATCH FOR InnoDB ENGINE (and future MyISAM Engine)
									if COMMITTRANSACTIONS == "YES":
										try:
											# PUNCH THE CHANGE IN
											sql_connect.commit()
										except:
											# REVERT
											sql_connect.rollback()
									# END PUSH THE ROW INTO THE DATABASE
									value_final = ''
								else:
									pass
							else:
								pass
							datestamp = datetime.now()
							datestamp = datestamp.strftime("%Y_%m%d_%H-%M-%S")
							if RECYCLE_COMM == 1:
								syphon_fault_recycle()
								print "Awaiting input on..."
								datestamp = datetime.now()
								datestamp = datestamp.strftime("%Y_%m%d_%H-%M-%S")
								print YOURDEVICENAME + " at " + datestamp
							else:
								print ""
								print "Awaiting next input on..."
								print YOURDEVICENAME + " at " + datestamp
								print ""
						# END KEEP RUNNING UNTIL WE HAVE A PROBLEM
						except:
							fault = "SY_RECYCLE"
							syphon_fault_recycle()
					# END PROCEED ONLY IF THE TELNET DEVICE CAN BE CONTACTED
					else:
						syphon_error_communication()
				# END PROCEED ONLY IF THE MySQL SERVER CAN BE CONTACTED
				else:
					syphon_error_sql()
				# CLOSE CONNECTION TO MySQL DB
				try:
					sql_cursor.close ()
					sql_connect.close ()
				except:
					if (REQUIRE_MYSQL == 1):
						syphon_error_sql_close()
					else:
						pass
			# PN ------------------ END GUTS_OF_ROUTINE --------------------- END PN
			else:
				syphon_error_options()
		else:
			syphon_error_command()
	else:
		print ""
		print "SKIPPING RUN_OPC ..."
#
#
# RUN_MATCH
	if YOURCOMMAND1 == 'RUN_MATCH':
		print ""
		print "STARTING ROUTINE - RUN_MATCH"
		if OK_RUN_MATCH >= 2:
		# -- RUN_MATCH
		# -- -- A ROUTINE TO READ TELNET DATE LINE BY LINE AND
		# -- -- THEN CHECK THAT DATA AGAINST A VALUE TO MATCH.
		# -- -- WHEN A MATCH IS FOUND, PUSH A KNOWN VALUE OUT
		# -- -- TO A mod_openopc DAEMON FOR WRITING TO A PLC
		# -- --  OR OTHER DEVICE.
		# -- -- YOURCOMMAND1 	... RUN_MATCH
		# -- -- YOUROPTION1	... PRESET FILE NAME wo EXTENSION
		# -- -- YOUROPTION2	... SEARCH | (blank)
		# -- -- YOUROPTION3	... LOG | (blank)
		# -- -- YOUROPTION4	... CONDITIONAL | (blank)
			#
			# SCAN ALL PRESETS AND OPTIONS
			try:
				pull_in_preset()
				# DECLARE THAT WE HAVE ACHIEVED A GOOD PRESET AND OPTIONS PULL
				OK_PRE_OPT_PULL = 1
				# NAME THIS THREAD
				THREADNAME = "syphon_RUN_MATCH_" + YOURDEVICENAME
				try:
					setproctitle.setproctitle(THREADNAME)	
				except:
					pass
			except:
				OK_PRE_OPT_PULL = 0
			#
			if OK_PRE_OPT_PULL == 1:
			# PN ------------------ BEGIN GUTS_OF_ROUTINE ------------------- END PN
				if (REQUIRE_MYSQL == 1):
					# CONNECT TO THE MySQL DATABASE
					try:
						# DEFINE WHAT IS USED AS A SPLITTER FOR MySQL PUSHES
						#   THIS IS ALWAYS A COMMA
						splitter = str(',')
						# INITIALIZE DATA DUMP HOLDING REGISTER
						value_final = ''
						fire_up_sql()
						mysql_is_down = 0
					except:
						mysql_is_down = 1
				else:
					pass
				# PROCEED ONLY IF THE MySQL SERVER CAN BE CONTACTED
				if ((mysql_is_down != 1) or (REQUIRE_MYSQL == 0)):
					# CONNECT TO THE TELNET DEVICE
					try:
						fire_up_telnet()
						telnet_is_down = 0
					except:
						telnet_is_down = 1
					# PROCEED ONLY IF THE DEVICE CAN BE CONTACTED
					while telnet_is_down != 1:
						try:	
							try:
								# -- READ EXPECT WITH A TIMEOUT
								RAWINPUT = tn.expect([YOURENDOFLINE],YOURTIMEOUT_INT)
								print "-- Value Incoming..."
								print " -- -- In RAW form..."
								print RAWINPUT
								INPUT1, INPUT2, INPUT3 = RAWINPUT
								print "-- -- In STRING form..."
								INPUT = str(RAWINPUT)
								INPUT1 = str(INPUT1)
								INPUT2 = str(INPUT2)
								INPUT3 = str(INPUT3)
								INPUT3 = INPUT3.replace(YOURENDOFLINE,'')
								print "-- -- -- INDEX: " + INPUT1
								print "-- -- -- MATCH: " + INPUT2
								print "-- -- -- VALUE: " + INPUT3
								if INPUT == 'EOFError':
									DROPPED = 1
									fault = "-- I/O miscommunication or Receive Error."
								else:
									if INPUT2 == 'None':
										DROPPED = 1
										fault = "-- Timeout, no data in " + YOURTIMEOUT + " seconds."
									else:
										DROPPED = 0
								CHECKING = 0
								if DROPPED == 0:
									CHECKING = 1
									INPUT_OUT = INPUT3[STARTCHAR:ENDCHAR]
									print "-- -- -- PARSED: " + INPUT_OUT
									print ""
									RECYCLE_COMM = 0
									# CHECK for NUMERIC VALUE
									if REQUIRENUMERICVALUE == 'yes':
										print "-- Checking for numeric data value..."
										try:
											TEST_NUMERIC = float(INPUT_OUT)
											print "-- -- data value IS numeric."
											print ""
											INPUT_OUT = float(INPUT_OUT)
											INPUT_OUT = str(INPUT_OUT)
										except:
											print "-- -- data value is NOT numeric."
											print "-- -- DISCARDING!"
											print ""
											DROPPED = 1
									else:
										print "-- Ignoring data type (string or numeric)..."
										print ""
									# CHECK for MATCH VALUE
									# -- MATCH EXACT OR SEARCH FOR ANY INSTANCE ?
									if YOUROPTION2 == 'SEARCH':
										# -- FIND ANY INSTANCE
										print "-- Checking for any instance of data value... (" + str(INPUT_OUT) + " ?contains? " + str(YOURMATCHVALUE) + ")"
										try:
											DROPPED_SEARCH = int(str(INPUT_OUT).count(str(YOURMATCHVALUE)))
											if DROPPED_SEARCH > 0:
												print "-- -- instance FOUND!"
												print ""
											else:
												print "-- -- instance not found."
												print"-- -- DISCARDING!"
												print ""
												DROPPED = 1
										except:
											print "-- -- fail to parse."
											print "-- -- DISCARDING!"
											print ""
											DROPPED = 1
									else:
										# -- EXACT MATCH
										print "-- Checking for match data value... (" + str(INPUT_OUT) + " =?= " + str(YOURMATCHVALUE) + ")"
										if str(YOURMATCHVALUE) == str(INPUT_OUT):
											print "-- -- match FOUND!"
											print ""
										else:
											print "-- -- match NOT found."
											print "-- -- DISCARDING!"
											print ""
											DROPPED = 1
										# PERFORM CONDITIONAL QUERY AND CHECK FOR CONDITIONAL MATCH
										if YOUROPTION4 == 'CONDITIONAL':
											print "-- Checking for condition required to handle data value..."
											trigger_query = "SELECT * FROM " + YOURDEVICETABLENAME + " WHERE " + YOURDEVICECOLUMNNAME + " LIKE \'" + YOURDEVICENAMEFORLOG + "\' ORDER BY DATESTAMP DESC LIMIT 1"
											trigger_query = str(trigger_query)
											print "-- -- Conditional value to test, incoming..."
					                                                print trigger_query
											sql_cursor.execute (trigger_query)
											# COMMIT QUERY TO DB
											# -- PATCH FOR InnoDB ENGINE (and future MyISAM Engine)
											if COMMITTRANSACTIONS == "YES":
												try:
													# PUNCH THE CHANGE IN
													sql_connect.commit()
												except:
													# REVERT
													sql_connect.rollback()
											value_trigger = sql_cursor.fetchone()
											value_trigger = value_trigger[2]
											value_trigger = str(value_trigger)
					                                                print value_trigger
											print "-- Checking for conditional match data value... (" + str(YOURCONDITIONALVALUE) + " =?= " + str(value_trigger) + ")"
											if str(YOURCONDITIONALVALUE) == str(value_trigger):
												print "-- -- match FOUND!"
												print ""
											else:
												print "-- -- match NOT found."
												print "-- -- DISCARDING!"
												print ""
												DROPPED = 1
								else:
									RECYCLE_COMM = 1
							except:
								INPUT_OUT = int(0)
								DROPPED = 1
								RECYCLE_COMM = 1
								fault = "-- Garbage Data Receive... Refreshing Connection."
							if DROPPED == 0:
								# IF INPUT IS NOT BAD THEN PUSH IT TO mod_openopc
								datestamp = datetime.now()
								datestamp = datestamp.strftime("%Y_%m%d_%H-%M-%S")
								FLATFILE = os.path.join(TEMPDIR, THREADNAME)
								FLATFILE = FLATFILE + "_" + datestamp + "_" + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + ".temp"
								print "-- built export file..."
								print FLATFILE
								FLATFILE_WORK = file(FLATFILE,'wt')
								FLATFILE_WORK = open(FLATFILE,'w')
								FLATFILE_CONTENT = "# START WRITE_DAEMON EVENT FILE FROM syphon.\n"
								FLATFILE_CONTENT = FLATFILE_CONTENT + "[your_write_type]\n"
								FLATFILE_CONTENT = FLATFILE_CONTENT + "YOURWRITETYPE:DECLARED\n"
								FLATFILE_CONTENT = FLATFILE_CONTENT + "# -- WRITE DECLARED VALUES TO OPC TARGET\n"
								FLATFILE_CONTENT = FLATFILE_CONTENT + "[your_leafers]\n"
								FLATFILE_CONTENT = FLATFILE_CONTENT + "YOURLEAFERS:"
								FLATFILE_CONTENT = FLATFILE_CONTENT + "XXX" + YOURTARGET + "YYY" + YOURLEAF + "&" + YOUREXECUTIONVALUE + "&|" + "\n"
								FLATFILE_CONTENT = FLATFILE_CONTENT + "YOURWRITEPRESET:NONE\n"
								FLATFILE_CONTENT = FLATFILE_CONTENT + "# -- NAME OF PRESET FILE TO WRITE\n"
								FLATFILE_CONTENT = FLATFILE_CONTENT + "# END OF FILE\n"
								FLATFILE_WORK.write(FLATFILE_CONTENT)
								FLATFILE_WORK.close()
								# MOVE THE TEMP FILE TO THE DAEMON IMPORT DIRECTORY
								EXPORT = os.path.join(PROGPATH_MODOPENOPC_GWCOMM, YOURMODOPENOPCDAEMON)
								EXPORT = os.path.join(EXPORT, THREADNAME)
								EXPORT = EXPORT + "_" + datestamp + "_" + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + ".event"
								shutil.move(FLATFILE,EXPORT)
								print "-- handed the file off to mod_openopc..."
							else:
								print "-- not exporting anything..."
							if ((RECYCLE_COMM == 0) and (CHECKING == 1)):
								if (YOUROPTION3 == 'LOG'):
									# IF INPUT IS NOT BAD THEN PUSH IT TO MySQL DATABASE TABLE
									datestamp = datetime.now()
									datestamp = datestamp.strftime("%Y_%m%d_%H:%M:%S")
									# ASSEMBLE THE FINAL VALUE FOR EXPORT (ALL FIELDS OF CHECKWEIGHER TABLE [DATA TABLE])
									value_final = "\'" + datestamp + "\'" + splitter + "\'" + YOURDEVICENAMEFORLOG + "\'" + splitter + "\'" + str(INPUT3) + "\'"
									# PUSH THE ROW INTO THE DATABASE
									# -- psuedo_query_example = INSERT INTO SQL_TABLE VALUES(value_final)
									sql_query = "INSERT INTO " + TABLE_SYPHON + " VALUES(" + value_final + ")"
									print ""
									print "NOTICE! -- EXPORTING RESULTS TO YOUR SQL TABLE - FOR..." + YOURDEVICENAMEFORLOG
									print "WE ARE USING THE FOLLOWING QUERY STRING..."
									print sql_query
									sql_query = str(sql_query)
									sql_cursor.execute (sql_query)
									# COMMIT QUERY TO DB
									# -- PATCH FOR InnoDB ENGINE (and future MyISAM Engine)
									if COMMITTRANSACTIONS == "YES":
										try:
											# PUNCH THE CHANGE IN
											sql_connect.commit()
										except:
											# REVERT
											sql_connect.rollback()
									# END PUSH THE ROW INTO THE DATABASE
									value_final = ''
								else:
									pass
							else:
								pass
							datestamp = datetime.now()
							datestamp = datestamp.strftime("%Y_%m%d_%H-%M-%S")
							if RECYCLE_COMM == 1:
								syphon_fault_recycle()
								datestamp = datetime.now()
								datestamp = datestamp.strftime("%Y_%m%d_%H-%M-%S")
								print "Awaiting input on..."
								print YOURDEVICENAME + " at " + datestamp
							else:
								print ""
								print "Awaiting next input on..."
								print YOURDEVICENAME + " at " + datestamp
								print ""
						# END KEEP RUNNING UNTIL WE HAVE A PROBLEM
						except:
							fault = "SY_RECYCLE"
							syphon_fault_recycle()
					# END PROCEED ONLY IF THE TELNET DEVICE CAN BE CONTACTED
					else:
						syphon_error_communication()
				# END PROCEED ONLY IF THE MySQL SERVER CAN BE CONTACTED
				else:
					syphon_error_sql()
				# CLOSE CONNECTION TO MySQL DB
				try:
					sql_cursor.close ()
					sql_connect.close ()
				except:
					if (REQUIRE_MYSQL == 1):
						syphon_error_sql_close()
					else:
						pass
			# PN ------------------ END GUTS_OF_ROUTINE --------------------- END PN
			else:
				syphon_error_options()
		else:
			syphon_error_command()
	else:
		print ""
		print "SKIPPING RUN_MATCH ..."
#
#
# RUN_CONDITIONAL_RETANSMIT
	if YOURCOMMAND1 == 'RUN_CONDITIONAL_RETRANSMIT':
		print ""
		print "STARTING ROUTINE - RUN_CONDITIONAL_RETRANSMIT"
		if OK_RUN_CONDITIONAL_RETRANSMIT >= 1:
		# -- RUN_MATCH
		# -- -- A ROUTINE TO READ TELNET DATA LINE BY LINE, THEN
		# -- -- QUERY A DB FOR A DEVICE STATUS FLAG.  IF THE STATUS
		# -- -- FLAG MATCHES A PRESET VALUE, THEN THE DATA READ VIA
		# -- -- TELNET WILL BE RETRANSMITTED TO A SECONDARY CLIENT
		# -- -- CONNECTED TO SYPHON VIA TELNET.  THINK OF IT AS
		# -- -- A MIDDLE MAN.
		# -- -- YOURCOMMAND1 	... RUN_CONDITIONAL_RETRANSMIT
		# -- -- YOUROPTION1	... PRESET FILE NAME wo EXTENSION
			#
			# SCAN ALL PRESETS AND OPTIONS
			try:
				pull_in_preset()
				# DECLARE THAT WE HAVE ACHIEVED A GOOD PRESET AND OPTIONS PULL
				OK_PRE_OPT_PULL = 1
				# NAME THIS THREAD
				THREADNAME = "syphon_RUN_COND_RETR_" + YOURDEVICENAME
				try:
					setproctitle.setproctitle(THREADNAME)	
				except:
					pass
			except:
				OK_PRE_OPT_PULL = 0
			#
			if OK_PRE_OPT_PULL == 1:
			# PN ------------------ BEGIN GUTS_OF_ROUTINE ------------------- END PN
				# INITIATE A SOCKET 
				# -- THIS IS BLOCKING IO SO WE CAN ONLY HAVE ONE SECONDARY CLIENT!
				while True:
					try: 
						# BUILD A SOCKET AND BIND TO IT
						BROADCAST_SOCKET = socket.socket()
						HOST_ADDRESS_PORT_COMBO = ('', int(YOURBROADCASTPORT))
						BROADCAST_SOCKET.bind(HOST_ADDRESS_PORT_COMBO)
						print "-- LISTENING ON PORT NUMBER " + str(YOURBROADCASTPORT)
						BROADCAST_SOCKET.listen(1)
						#
						# WAIT FOR A CLIENT TO REQUEST ACCEPTANCE OF NEW CONNECTION
						# TO YOUR BROADCAST PORT
						BROADCAST_CLIENT_LOST = 0
						while BROADCAST_CLIENT_LOST == 0:
							# REPEATEDLY TRY TO ACCEPT NEW CONNECTIONS FROM CLIENTS
							BROADCAST_ADDRESS_CLIENT = ''
							BROADCAST_CONNECTION, BROADCAST_ADDRESS_CLIENT = BROADCAST_SOCKET.accept()
							# DON'T WASTE RESOURCES BY DOING JOB IF WE DO NOT HAVE ANY CLIENT CONNECTED
							# OR IF CLIENT DISCONNECTS
							# -- CHECK FOR BROADCAST_ADDRESS_CLIENT VALUE AND BROADCAST_CLIENT_LOST VALUE
							while (BROADCAST_ADDRESS_CLIENT != '') and (BROADCAST_CLIENT_LOST == 0):
								# CONNECT TO THE MySQL DATABASE
								try:
									# DEFINE WHAT IS USED AS A SPLITTER FOR MySQL PUSHES
									#   THIS IS ALWAYS A COMMA
									splitter = str(',')
									# INITIALIZE DATA DUMP HOLDING REGISTER
									value_final = ''
									fire_up_sql()
									mysql_is_down = 0
								except:
									mysql_is_down = 1
								# PROCEED ONLY IF THE MySQL SERVER CAN BE CONTACTED
								if mysql_is_down != 1:
									# CONNECT TO THE TELNET DEVICE
									try:
										fire_up_telnet()
										telnet_is_down = 0
									except:
										telnet_is_down = 1
									# PROCEED ONLY IF THE DEVICE CAN BE CONTACTED
									while (telnet_is_down != 1) and (BROADCAST_CLIENT_LOST == 0):
										try:	
											try:	
												# -- READ EXPECT WITH A TIMEOUT
												RAWINPUT = tn.expect([YOURENDOFLINE],YOURTIMEOUT_INT)
												print "-- Value Incoming..."
												print " -- -- In RAW form..."
												print RAWINPUT
												INPUT1, INPUT2, INPUT3 = RAWINPUT
												print "-- -- In STRING form..."
												INPUT = str(RAWINPUT)
												INPUT1 = str(INPUT1)
												INPUT2 = str(INPUT2)
												INPUT3 = str(INPUT3)
												INPUT3 = INPUT3.replace(YOURENDOFLINE,'')
												print "-- -- -- INDEX: " + INPUT1
												print "-- -- -- MATCH: " + INPUT2
												print "-- -- -- VALUE: " + INPUT3
												if INPUT == 'EOFError':
													DROPPED = 1
													fault = "-- I/O miscommunication or Receive Error."
												else:
													if INPUT2 == 'None':
														DROPPED = 1
														fault = "-- Timeout, no data in " + YOURTIMEOUT + " seconds."
													else:
														DROPPED = 0
												if DROPPED == 0:
													INPUT_OUT = INPUT3[STARTCHAR:ENDCHAR]
													print "-- -- -- PARSED: " + INPUT_OUT
													print ""
													RECYCLE_COMM = 0
													# CHECK for NUMERIC VALUE
													if REQUIRENUMERICVALUE == 'yes':
														print "-- Checking for numeric data value..."
														try:
															TEST_NUMERIC = float(INPUT_OUT)
															print "-- -- data value IS numeric."
															print ""
															INPUT_OUT = float(INPUT_OUT)
															INPUT_OUT = str(INPUT_OUT)
														except:
															print "-- -- data value is NOT numeric."
															print "-- -- DISCARDING!"
															print ""
															DROPPED = 1
													else:
														print "-- Ignoring data type (string or numeric)..."
														print ""
													# CHECK for MATCH OF TRIGGER OR STATUS VALUE
													# -- EXACT MATCH
													# -- -- WAIT SPECIFIED TIME BEFORE POLLING TRIGGER VALUE
													time.sleep(float(YOURMATCHWAIT))
													# -- -- PULL FROM
													trigger_query = "SELECT * FROM " + TABLE_SYPHON + " WHERE " + YOURDEVICECOLUMNNAME + " LIKE \'" + YOURDEVICENAMEFORLOG + "\' ORDER BY DATESTAMP DESC LIMIT 1"
													trigger_query = str(trigger_query)
													print "-- -- Trigger value to test, incoming..."
						                                                        print trigger_query
													sql_cursor.execute (trigger_query)
													# COMMIT QUERY TO DB
													# -- PATCH FOR InnoDB ENGINE (and future MyISAM Engine)
													if COMMITTRANSACTIONS == "YES":
														try:
															# PUNCH THE CHANGE IN
															sql_connect.commit()
														except:
															# REVERT
															sql_connect.rollback()
													value_trigger = sql_cursor.fetchone()
													value_trigger = value_trigger[2]
													value_trigger = str(value_trigger)
						                                                        print value_trigger
													print "-- Checking for trigger match data value... (" + str(YOURMATCHVALUE) + " =?= " + str(value_trigger) + ")"
													if str(YOURMATCHVALUE) == str(value_trigger):
														print "-- -- trigger match FOUND!"
														print ""
													else:
														print "-- -- trigger match NOT found."
														print "-- -- DISCARDING!"
														print ""
														DROPPED = 1
												else:
													RECYCLE_COMM = 1
											except:
												INPUT_OUT = int(0)
												DROPPED = 1
												RECYCLE_COMM = 1
												fault = "-- Garbage Data Receive... Refreshing Connection."
											if DROPPED == 0:
												# IF INPUT IS NOT BAD PUSH THE BROADCAST DATA TO CONNECTED CLIENT
												try:
													BROADCAST_DATA_TO_SEND = str(INPUT_OUT)
													print "broadcasting... " + BROADCAST_DATA_TO_SEND
													BROADCAST_CONNECTION.send(BROADCAST_DATA_TO_SEND + '\r\n')
													print "-- data broadcast to client - ok..."
												except:
													print "-- Connection to Broadcast Client lost - freeing resources."
													try:
														BROADCAST_CONNECTION.close()
													except:
														pass
													BROADCAST_CLIENT_LOST = 1
											else:
												# IF INPUT IS BAD, EMPTY OR TIMED OUT, PUSH KEEP ALIVE TO CONNECTED CLIENT
												try:
													BROADCAST_DATA_TO_SEND = "KEEP_ALIVE"
													print "broadcasting... " + BROADCAST_DATA_TO_SEND
													BROADCAST_CONNECTION.send(BROADCAST_DATA_TO_SEND + '\r\n')
													print "-- sending only keepalive to client - ok..."
												except:
													print "-- Connection to Broadcast Client lost - freeing resources."
													try:
														BROADCAST_CONNECTION.close()
													except:
														pass
													BROADCAST_CLIENT_LOST = 1
											datestamp = datetime.now()
											datestamp = datestamp.strftime("%Y_%m%d_%H-%M-%S")
											if (RECYCLE_COMM == 1) and (BROADCAST_CLIENT_LOST == 0):
												syphon_fault_recycle()
												datestamp = datetime.now()
												datestamp = datestamp.strftime("%Y_%m%d_%H-%M-%S")
												print "Awaiting input on..."
												print YOURDEVICENAME + " at " + datestamp
											else:
												if (RECYCLE_COMM == 1):
													# -- CLOSE THE telnet CONNECTION
													datestamp = datetime.now()
													datestamp = datestamp.strftime("%Y_%m%d_%H-%M-%S")
													try:
														tn.close()
														print ""
														print "-- TELNET CONNECTION CLOSED at " + datestamp
														print ""
													except:
														print ""
														print "-- Failure to close connetion to Telnet Device,"
														print "hard drop will follow at " + datestamp
													# -- WAIT
													time.sleep(0.5)
												else:
													print ""
													print "Awaiting next input on..."
													print YOURDEVICENAME + " at " + datestamp
													print ""
										# END KEEP RUNNING UNTIL WE HAVE A PROBLEM
										except:
											fault = "SY_RECYCLE"
											syphon_fault_recycle()
									# END PROCEED ONLY IF THE TELNET DEVICE CAN BE CONTACTED
									else:
										if (BROADCAST_CLIENT_LOST == 0):
											syphon_error_communication()
										else:
											pass
								# END PROCEED ONLY IF THE MySQL SERVER CAN BE CONTACTED
								else:
									syphon_error_sql()
								# CLOSE CONNECTION TO MySQL DB
								try:
									sql_cursor.close ()
									sql_connect.close ()
								except:
									syphon_error_sql_close()
							# SLEEP JUST A MOMENT IF WE DON'T HAVE A CLIENT
							time.sleep(0.1)
					except:
						# MICROSCOPIC SLEEP TIME GIVES US ABILITY TO DIE ON 
						# EXCEPTIONS GENERATED FROM KEYSTROKE
						try:
							BROADCAST_CONNECTION.close()
						except:
							pass
						try:
							BROADCAST_SOCKET.close()
						except:
							pass
						time.sleep(0.1)
			# PN ------------------ END GUTS_OF_ROUTINE --------------------- END PN
			else:
				syphon_error_options()
		else:
			syphon_error_command()
	else:
		print ""
		print "SKIPPING RUN_CONDITIONAL_RETRANSMIT ..."
#
#
# RUN_SEER_CHECKWEIGHERMODEL_V1
	if YOURCOMMAND1 == 'RUN_SEER_CHECKWEIGHERMODEL_V1':
		print ""
		print "STARTING ROUTINE - RUN_SEER_CHECKWEIGHERMODEL_V1"
		if OK_RUN_SEER_CHECKWEIGHERMODEL_V1 >= 1:
		# -- RUN_SEER_CHECKWEIGHERMODEL_V1
		# -- -- A ROUTINE TO READ TELNET DATA LINE BY LINE AND
		# -- -- THEN PUSH THAT DATA OUT TO A MySQL DATABASE
		# -- -- ALL THE WHILE GUIDED BY SEER.
		# -- -- YOURCOMMAND1 	... RUN_SEER_CHECKWEIGHERMODEL_V1
		# -- -- YOUROPTION1	... PRESET FILE NAME wo EXTENSION
			#
			# SCAN ALL PRESETS AND OPTIONS
			try:
				pull_in_preset()
				# DECLARE THAT WE HAVE ACHIEVED A GOOD PRESET AND OPTIONS PULL
				OK_PRE_OPT_PULL = 1
				# NAME THIS THREAD
				THREADNAME = "syphon_SEER_CW_v1_" + YOURDEVICENAME
				try:
					setproctitle.setproctitle(THREADNAME)	
				except:
					pass
			except:
				OK_PRE_OPT_PULL = 0
			#
			if OK_PRE_OPT_PULL == 1:
			# PN ------------------ BEGIN GUTS_OF_ROUTINE ------------------- END PN
				# CONNECT TO THE MySQL DATABASE
				try:
					# DEFINE WHAT IS USED AS A SPLITTER FOR MySQL PUSHES
					#   THIS IS ALWAYS A COMMA
					splitter = str(',')
					# INITIALIZE DATA DUMP HOLDING REGISTER
					value_final = ''
					fire_up_sql()
					mysql_is_down = 0
				except:
					mysql_is_down = 1
				# PROCEED ONLY IF THE MySQL SERVER CAN BE CONTACTED
				if mysql_is_down != 1:
					# CONNECT TO THE TELNET DEVICE
					try:
						fire_up_telnet()
						telnet_is_down = 0
					except:
						telnet_is_down = 1
					# PROCEED ONLY IF THE DEVICE CAN BE CONTACTED
					while telnet_is_down != 1:
						try:	
							try:
								# -- READ EXPECT WITH A TIMEOUT
								RAWINPUT = tn.expect([YOURENDOFLINE],YOURTIMEOUT_INT)
								print "-- Value Incoming..."
								print " -- -- In RAW form..."
								print RAWINPUT
								INPUT1, INPUT2, INPUT3 = RAWINPUT
								print "-- -- In STRING form..."
								INPUT = str(RAWINPUT)
								INPUT1 = str(INPUT1)
								INPUT2 = str(INPUT2)
								INPUT3 = str(INPUT3)
								INPUT3 = INPUT3.replace(YOURENDOFLINE,'')
								print "-- -- -- INDEX: " + INPUT1
								print "-- -- -- MATCH: " + INPUT2
								print "-- -- -- VALUE: " + INPUT3
								if INPUT == 'EOFError':
									DROPPED = 1
									fault = "-- I/O miscommunication or Receive Error."
								else:
									if INPUT2 == 'None':
										DROPPED = 1
										fault = "-- Timeout, no data in " + YOURTIMEOUT + " seconds."
									else:
										DROPPED = 0
								if DROPPED == 0:
									INPUT_OUT = INPUT3[STARTCHAR:ENDCHAR]
									print "-- -- -- PARSED: " + INPUT_OUT
									print ""
									RECYCLE_COMM = 0
									# CHECK for NUMERIC VALUE
									if REQUIRENUMERICVALUE == 'yes':
										print "-- Checking for numeric data value..."
										try:
											TEST_NUMERIC = float(INPUT_OUT)
											print "-- -- data value IS numeric."
											print ""
											INPUT_OUT = float(INPUT_OUT)
											INPUT_OUT = str(INPUT_OUT)
										except:
											print "-- -- data value is NOT numeric."
											print "-- -- DISCARDING!"
											print ""
											DROPPED = 1
									else:
										print "-- Ignoring data type (string or numeric)..."
										print ""
								else:
									RECYCLE_COMM = 1
							except:
								INPUT_OUT = int(0)
								DROPPED = 1
								RECYCLE_COMM = 1
								fault = "-- Garbage Data Receive... Refreshing Connection."
							if DROPPED == 0:
								# IF INPUT IS NOT BAD THEN PUSH IT TO MySQL DATABASE TABLE
								datestamp = datetime.now()
								datestamp = datestamp.strftime("%Y_%m%d_%H:%M:%S")
								# SCALE THE INPUT AS NEEDED
								INPUT_OUT = float(INPUT_OUT) * float(YOURSCALEFACTOR)
								INPUT_OUT = str(INPUT_OUT)
								# PULL THE ACTIVE RECIPE IN FROM THE CHECKWEIGHERMODEL 'SYPHON' TABLE
								comment_query = "SELECT * FROM " + CHECKWEIGHERMODEL_TABLE_SYPHON + " WHERE MACHINENAME LIKE \'" + YOURDEVICENAMEFORLOG + "\'"
								comment_query = str(comment_query)
								print "Active RECIPE string incoming..."
	                                                        print comment_query
								sql_cursor.execute (comment_query)
								# COMMIT QUERY TO DB
								# -- PATCH FOR InnoDB ENGINE (and future MyISAM Engine)
								if COMMITTRANSACTIONS == "YES":
									try:
										# PUNCH THE CHANGE IN
										sql_connect.commit()
									except:
										# REVERT
										sql_connect.rollback()
								value_comment = sql_cursor.fetchone()
								value_comment = value_comment[1]
								value_comment = str(value_comment)
	                                                        print value_comment
								# ASSEMBLE THE FINAL VALUE FOR EXPORT (ALL FIELDS OF CHECKWEIGHER TABLE [DATA TABLE])
								value_final = "\'" + datestamp + "\'" + splitter + "\'" + YOURDEVICENAMEFORLOG + "\'" + splitter + "\'" + INPUT_OUT + "\'" + splitter + "\'" + value_comment + "\'"
								# PUSH THE ROW INTO THE DATABASE
								# -- psuedo_query_example = INSERT INTO SQL_TABLE VALUES(value_final)
								sql_query = "INSERT INTO " + CHECKWEIGHERMODEL_TABLE + " VALUES(" + value_final + ")"
								print ""
								print "NOTICE! -- EXPORTING RESULTS TO YOUR SQL TABLE - FOR..." + YOURDEVICENAMEFORLOG
								print "WE ARE USING THE FOLLOWING QUERY STRING..."
								print sql_query
								sql_query = str(sql_query)
								sql_cursor.execute (sql_query)
								# COMMIT QUERY TO DB
								# -- PATCH FOR InnoDB ENGINE (and future MyISAM Engine)
								if COMMITTRANSACTIONS == "YES":
									try:
										# PUNCH THE CHANGE IN
										sql_connect.commit()
									except:
										# REVERT
										sql_connect.rollback()
								# END PUSH THE ROW INTO THE DATABASE
								value_final = ''
							else:
								print "-- not exporting anything..."
							datestamp = datetime.now()
							datestamp = datestamp.strftime("%Y_%m%d_%H:%M:%S")
							if RECYCLE_COMM == 1:
								# KEEP ALIVE FUNCTION
								print ""
								print "Executing 'keep-alive' instructions..."
								syphon_fault_recycle()
								print "Awaiting input on..."
								datestamp = datetime.now()
								datestamp = datestamp.strftime("%Y_%m%d_%H-%M-%S")
								print YOURDEVICENAME + " at " + datestamp
							else:
								print ""
								print "Awaiting next input on..."
								print YOURDEVICENAME + " at " + datestamp
								print ""
						# END KEEP RUNNING UNTIL WE HAVE A PROBLEM
						except:
							syphon_fault_recycle()
					# END PROCEED ONLY IF THE TELNET DEVICE CAN BE CONTACTED
					else:
						syphon_error_communication()
				# END PROCEED ONLY IF THE MySQL SERVER CAN BE CONTACTED
				else:
					syphon_error_sql()
				# CLOSE CONNECTION TO MySQL DB
				try:
					sql_cursor.close ()
					sql_connect.close ()
				except:
					syphon_error_sql_close()
			# PN ------------------ END GUTS_OF_ROUTINE --------------------- END PN
			else:
				syphon_error_options()
		else:
			syphon_error_command()
	else:
		print ""
		print "SKIPPING RUN_SEER_CHECKWEIGHERMODEL_V1 ..."
#
#
# RUN_SEER_CHECKWEIGHERMODEL_V2
	if YOURCOMMAND1 == 'RUN_SEER_CHECKWEIGHERMODEL_V2':
		print ""
		print "STARTING ROUTINE - RUN_SEER_CHECKWEIGHERMODEL_V2"
		if OK_RUN_SEER_CHECKWEIGHERMODEL_V2 >= 1:
		# -- RUN_SEER_CHECKWEIGHERMODEL_V2
		# -- -- A ROUTINE TO READ TELNET DATE LINE BY LINE AND
		# -- -- THEN PUSH THAT DATA OUT TO A MySQL DATABASE
		# -- -- ALL THE WHILE GUIDED BY SEER.
		# -- -- YOURCOMMAND1 	... RUN_SEER_CHECKWEIGHERMODEL_V1
		# -- -- YOUROPTION1	... PRESET FILE NAME wo EXTENSION
			#
			# SCAN ALL PRESETS AND OPTIONS
			try:
				pull_in_preset()
				# DECLARE THAT WE HAVE ACHIEVED A GOOD PRESET AND OPTIONS PULL
				OK_PRE_OPT_PULL = 1
				# NAME THIS THREAD
				THREADNAME = "syphon_SEER_CW_v2_" + YOURDEVICENAME
				try:
					setproctitle.setproctitle(THREADNAME)	
				except:
					pass
			except:
				OK_PRE_OPT_PULL = 0
			#
			if OK_PRE_OPT_PULL == 1:
			# PN ------------------ BEGIN GUTS_OF_ROUTINE ------------------- END PN
				# CONNECT TO THE MySQL DATABASE
				try:
					# DEFINE WHAT IS USED AS A SPLITTE FOR MySQL PUSHES
					#   THIS IS ALWAYS A COMMA
					splitter = str(',')
					# INITIALIZE DATA DUMP HOLDING REGISTER
					value_final = ''
					fire_up_sql()
					mysql_is_down = 0
				except:
					mysql_is_down = 1
				# PROCEED ONLY IF THE MySQL SERVER CAN BE CONTACTED
				if mysql_is_down != 1:
					# CONNECT TO THE TELNET DEVICE
					try:
						fire_up_telnet()
						telnet_is_down = 0
					except:
						telnet_is_down = 1
					# PROCEED ONLY IF THE DEVICE CAN BE CONTACTED
					while telnet_is_down != 1:
						try:	
							try:
								# -- READ EXPECT WITH A TIMEOUT
								RAWINPUT = tn.expect([YOURENDOFLINE],YOURTIMEOUT_INT)
								print "-- Value Incoming..."
								print " -- -- In RAW form..."
								print RAWINPUT
								INPUT1, INPUT2, INPUT3 = RAWINPUT
								print "-- -- In STRING form..."
								INPUT = str(RAWINPUT)
								INPUT1 = str(INPUT1)
								INPUT2 = str(INPUT2)
								INPUT3 = str(INPUT3)
								INPUT3 = INPUT3.replace(YOURENDOFLINE,'')
								print "-- -- -- INDEX: " + INPUT1
								print "-- -- -- MATCH: " + INPUT2
								print "-- -- -- VALUE: " + INPUT3
								if INPUT == 'EOFError':
									DROPPED = 1
									fault = "-- I/O miscommunication or Receive Error."
								else:
									if INPUT2 == 'None':
										DROPPED = 1
										fault = "-- Timeout, no data in " + YOURTIMEOUT + " seconds."
									else:
										DROPPED = 0
								if DROPPED == 0:
									INPUT_OUT = INPUT3[STARTCHAR:ENDCHAR]
									print "-- -- -- PARSED: " + INPUT_OUT
									print ""
									RECYCLE_COMM = 0
									# CHECK for NUMERIC VALUE
									if REQUIRENUMERICVALUE == 'yes':
										print "-- Checking for numeric data value..."
										try:
											TEST_NUMERIC = float(INPUT_OUT)
											print "-- -- data value IS numeric."
											print ""
											INPUT_OUT = float(INPUT_OUT)
											INPUT_OUT = str(INPUT_OUT)
										except:
											print "-- -- data value is NOT numeric."
											print "-- -- DISCARDING!"
											print ""
											DROPPED = 1
									else:
										print "-- Ignoring data type (string or numeric)..."
										print ""
								else:
									RECYCLE_COMM = 1
							except:
								INPUT_OUT = int(0)
								DROPPED = 1
								RECYCLE_COMM = 1
								fault = "-- Garbage Data Receive... Refreshing Connection."
							if DROPPED == 0:
								# IF INPUT IS NOT BAD THEN PUSH IT TO MySQL DATABASE TABLE
								datestamp = datetime.now()
								datestamp = datestamp.strftime("%Y_%m%d_%H:%M:%S")
								# SCALE THE INPUT AS NEEDED
								INPUT_OUT = float(INPUT_OUT) * float(YOURSCALEFACTOR)
								INPUT_OUT = str(INPUT_OUT)
								# PULL THE ACTIVE RECIPE IN FROM THE CHECKWEIGHERMODEL 'SYPHON' TABLE
								comment_query = "SELECT * FROM " + CHECKWEIGHERMODEL_TABLE_SYPHON + " WHERE MACHINENAME LIKE \'" + YOURDEVICENAMEFORLOG + "\'"
								comment_query = str(comment_query)
								print "Active RECIPE string incoming..."
	                                                        print comment_query
								sql_cursor.execute (comment_query)
								# COMMIT QUERY TO DB
								# -- PATCH FOR InnoDB ENGINE (and future MyISAM Engine)
								if COMMITTRANSACTIONS == "YES":
									try:
										# PUNCH THE CHANGE IN
										sql_connect.commit()
									except:
										# REVERT
										sql_connect.rollback()
								value_fetched = sql_cursor.fetchone()
								value_comment = value_fetched[1]
								value_comment = str(value_comment)
								value_operator = value_fetched[2]
								value_operator = str(value_operator)
	                                                        print value_comment
								# ASSEMBLE THE FINAL VALUE FOR EXPORT (ALL FIELDS OF CHECKWEIGHER TABLE [DATA TABLE])
								value_final = "\'" + datestamp + "\'" + splitter + "\'" + YOURDEVICENAMEFORLOG + "\'" + splitter + "\'" + INPUT_OUT + "\'" + splitter + "\'" + value_comment + "\'" + splitter + "\'" + value_operator + "\'"
								# PUSH THE ROW INTO THE DATABASE
								# -- psuedo_query_example = INSERT INTO SQL_TABLE VALUES(value_final)
								sql_query = "INSERT INTO " + CHECKWEIGHERMODEL_TABLE + " VALUES(" + value_final + ")"
								print ""
								print "NOTICE! -- EXPORTING RESULTS TO YOUR SQL TABLE - FOR..." + YOURDEVICENAMEFORLOG
								print "WE ARE USING THE FOLLOWING QUERY STRING..."
								print sql_query
								sql_query = str(sql_query)
								sql_cursor.execute (sql_query)
								# COMMIT QUERY TO DB
								# -- PATCH FOR InnoDB ENGINE (and future MyISAM Engine)
								if COMMITTRANSACTIONS == "YES":
									try:
										# PUNCH THE CHANGE IN
										sql_connect.commit()
									except:
										# REVERT
										sql_connect.rollback()
								# END PUSH THE ROW INTO THE DATABASE
								value_final = ''
							else:
								print "-- not exporting anything..."
							datestamp = datetime.now()
							datestamp = datestamp.strftime("%Y_%m%d_%H:%M:%S")
							if RECYCLE_COMM == 1:
								# KEEP ALIVE FUNCTION
								print ""
								print "Executing MySQL 'keep-alive' instructions..."
								syphon_fault_recycle()
								RECYCLE_COMM = 0
								print "Awaiting input on..."
								datestamp = datetime.now()
								datestamp = datestamp.strftime("%Y_%m%d_%H-%M-%S")
								print YOURDEVICENAME + " at " + datestamp
							else:
								print ""
								print "Awaiting next input on..."
								print YOURDEVICENAME + " at " + datestamp
								print ""
						# END KEEP RUNNING UNTIL WE HAVE A PROBLEM
						except:
							syphon_fault_recycle()
					# END PROCEED ONLY IF THE TELNET DEVICE CAN BE CONTACTED
					else:
						syphon_error_communication()
				# END PROCEED ONLY IF THE MySQL SERVER CAN BE CONTACTED
				else:
					syphon_error_sql()
				# CLOSE CONNECTION TO MySQL DB
				try:
					sql_cursor.close ()
					sql_connect.close ()
				except:
					syphon_error_sql_close()

			# PN ------------------ END GUTS_OF_ROUTINE --------------------- END PN
			else:
				syphon_error_options()
		else:
			syphon_error_command()
	else:
		print ""
		print "SKIPPING RUN_SEER_CHECKWEIGHERMODEL_V2 ..."
#
#
# RUN_SEER_WARRIOR_EOR_ACQUIRE
	if YOURCOMMAND1 == 'RUN_SEER_WARRIOR_EOR_ACQUIRE':
		print ""
		print "STARTING ROUTINE - RUN_SEER_WARRIOR_EOR_ACQUIRE"
		if OK_RUN_SEER_WARRIOR_EOR_ACQUIRE >= 1:
		# -- RUN_SEER_WARRIOR_EOR_ACQUIRE
		# -- -- A ROUTINE TO READ TELNET DATA LINE BY LINE AND
		# -- -- THEN USE THAT DATA TO UPDATE FIELDS IN A MySQL DATABASE
		# -- -- ALL THE WHILE GUIDED BY SEER.
		# -- -- -- ONLY COMPATIBLE WITH SEER INSTALLATIONS RUNNING THE
		#	   WARRIOR MODULE (as of v2 - 2011/08/01 and later)
		#	   WITH THE 'lactalis_bartender_labeling_system' PLUGIN
		# -- -- YOURCOMMAND1 	... RUN_SEER_WARRIOR_EOR_ACQUIRE
		# -- -- YOUROPTION1	... PRESET FILE NAME wo EXTENSION
			#
			# SCAN ALL PRESETS AND OPTIONS
			try:
				pull_in_preset()
				# DECLARE THAT WE HAVE ACHIEVED A GOOD PRESET AND OPTIONS PULL
				OK_PRE_OPT_PULL = 1
				# NAME THIS THREAD
				THREADNAME = "syphon_SEER_WAR_EOR_AQ_" + YOURDEVICENAME
				try:
					setproctitle.setproctitle(THREADNAME)	
				except:
					pass
			except:
				OK_PRE_OPT_PULL = 0
			#
			if OK_PRE_OPT_PULL == 1:
			# PN ------------------ BEGIN GUTS_OF_ROUTINE ------------------- END PN
				# CONNECT TO THE MySQL DATABASE
				try:
					# DEFINE WHAT IS USED AS A SPLITTE FOR MySQL PUSHES
					#   THIS IS ALWAYS A COMMA
					splitter = str(',')
					# INITIALIZE DATA DUMP HOLDING REGISTER
					value_final = ''
					fire_up_sql()
					mysql_is_down = 0
				except:
					mysql_is_down = 1
				# PROCEED ONLY IF THE MySQL SERVER CAN BE CONTACTED
				if mysql_is_down != 1:
					# CONNECT TO THE TELNET DEVICE
					try:
						fire_up_telnet()
						telnet_is_down = 0
					except:
						telnet_is_down = 1
					# PROCEED ONLY IF THE DEVICE CAN BE CONTACTED
					while telnet_is_down != 1:
						try:	
							try:
								# -- READ EXPECT WITH A TIMEOUT
								RAWINPUT = tn.expect([YOURENDOFLINE],YOURTIMEOUT_INT)
								print "-- Value Incoming..."
								print " -- -- In RAW form..."
								print RAWINPUT
								INPUT1, INPUT2, INPUT3 = RAWINPUT
								print "-- -- In STRING form..."
								INPUT = str(RAWINPUT)
								INPUT1 = str(INPUT1)
								INPUT2 = str(INPUT2)
								INPUT3 = str(INPUT3)
								INPUT3 = INPUT3.replace(YOURENDOFLINE,'')
								print "-- -- -- INDEX: " + INPUT1
								print "-- -- -- MATCH: " + INPUT2
								print "-- -- -- VALUE: " + INPUT3
								if INPUT == 'EOFError':
									DROPPED = 1
									fault = "-- I/O miscommunication or Receive Error."
								else:
									if INPUT2 == 'None':
										DROPPED = 1
										fault = "-- Timeout, no data in " + YOURTIMEOUT + " seconds."
									else:
										DROPPED = 0
								if DROPPED == 0:
									INPUT_OUT = INPUT3[STARTCHAR:ENDCHAR]
									print "-- -- -- PARSED: " + INPUT_OUT
									print ""
									RECYCLE_COMM = 0
									# CHECK for NUMERIC VALUE
									if REQUIRENUMERICVALUE == 'yes':
										print "-- Checking for numeric data value..."
										try:
											TEST_NUMERIC = int(INPUT_OUT)
											print "-- -- data value IS numeric."
											print ""
											INPUT_OUT = int(INPUT_OUT)
										except:
											print "-- -- data value is NOT numeric."
											print "-- -- DISCARDING!"
											print ""
											DROPPED = 1
									else:
										print "-- Ignoring data type (string or numeric)..."
										print ""
								else:
									RECYCLE_COMM = 1
							except:
								INPUT_OUT = int(0)
								DROPPED = 1
								RECYCLE_COMM = 1
								fault = "-- Garbage Data Receive... Refreshing Connection."
							if DROPPED == 0:
								# IF INPUT IS NOT BAD THEN PUSH IT TO MySQL DATABASE TABLE
								datestamp = datetime.now()
								datestamp = datestamp.strftime("%Y_%m%d_%H:%M:%S")
								# ASSEMBLE THE FINAL VALUE FOR EXPORT (IN THIS CASE THE VALUE CONSISTS OF ONLY THE VARIABLE 'INPUT_OUT')
								value_final = str(INPUT_OUT)
								# PUSH THE ROW INTO THE DATABASE
								# -- psuedo_query_example = UPDATE EOR_TABLE SET EOR_PENDING='value_final' WHERE LINE='YOURDEVICENAMEFORLOG'
								sql_query = "UPDATE " + EOR_TABLE + " SET EOR_PENDING='" + value_final + "' WHERE LINE='" + YOURDEVICENAMEFORLOG + "'"
								print ""
								print "NOTICE! -- UPDATING EOR INSIDE YOUR SQL TABLE - FOR..." + YOURDEVICENAME
								print "WE ARE USING THE FOLLOWING QUERY STRING..."
								print sql_query
								sql_query = str(sql_query)
								sql_cursor.execute (sql_query)
								# COMMIT QUERY TO DB
								# -- PATCH FOR InnoDB ENGINE (and future MyISAM Engine)
								if COMMITTRANSACTIONS == "YES":
									try:
										# PUNCH THE CHANGE IN
										sql_connect.commit()
									except:
										# REVERT
										sql_connect.rollback()
								# END PUSH THE ROW INTO THE DATABASE
								value_final = ''
							else:
								print "-- not exporting anything..."
							datestamp = datetime.now()
							datestamp = datestamp.strftime("%Y_%m%d_%H:%M:%S")
							if RECYCLE_COMM == 1:
								# KEEP ALIVE FUNCTION
								print ""
								print "Executing MySQL 'keep-alive' instructions..."
								syphon_fault_recycle()
								RECYCLE_COMM = 0
								print "Awaiting input on..."
								datestamp = datetime.now()
								datestamp = datestamp.strftime("%Y_%m%d_%H-%M-%S")
								print YOURDEVICENAME + " at " + datestamp
							else:
								print ""
								print "Awaiting next input on..."
								print YOURDEVICENAME + " at " + datestamp
								print ""
						# END KEEP RUNNING UNTIL WE HAVE A PROBLEM
						except:
							syphon_fault_recycle()
					# END PROCEED ONLY IF THE TELNET DEVICE CAN BE CONTACTED
					else:
						syphon_error_communication()
				# END PROCEED ONLY IF THE MySQL SERVER CAN BE CONTACTED
				else:
					syphon_error_sql()
				# CLOSE CONNECTION TO MySQL DB
				try:
					sql_cursor.close ()
					sql_connect.close ()
				except:
					syphon_error_sql_close()
			# PN ------------------ END GUTS_OF_ROUTINE --------------------- END PN
			else:
				syphon_error_options()
		else:
			syphon_error_command()
	else:
		print ""
		print "SKIPPING RUN_SEER_WARRIOR_EOR_ACQUIRE ..."
#
#
#
# RUN_SEER_WARRIOR_EOR_EXECUTE
	if YOURCOMMAND1 == 'RUN_SEER_WARRIOR_EOR_EXECUTE':
		print ""
		print "STARTING ROUTINE - RUN_SEER_WARRIOR_EOR_EXECUTE"
		if OK_RUN_SEER_WARRIOR_EOR_EXECUTE >= 1:
		# -- RUN_SEER_WARRIOR_EOR_EXECUTE
		# -- -- A ROUTINE TO READ TELNET DATA LINE BY LINE AND
		# -- -- THEN USE THAT DATA TO COMPARE TO FIELDS IN A MySQL DATABASE
		# -- -- AND UPON SUCCESSFUL MATCH, WRITE A VALUE TO A SPECIFIED 
		# -- -- OPC DEVICE.
		# -- -- YOURCOMMAND1 	... RUN_SEER_WARRIOR_EOR_EXECUTE
		# -- -- YOUROPTION1	... PRESET FILE NAME wo EXTENSION
			#
			# SCAN ALL PRESETS AND OPTIONS
			try:
				pull_in_preset()
				# DECLARE THAT WE HAVE ACHIEVED A GOOD PRESET AND OPTIONS PULL
				OK_PRE_OPT_PULL = 1
				# NAME THIS THREAD
				THREADNAME = "syphon_SEER_WAR_EOR_EXEC_" + YOURDEVICENAME
				try:
					setproctitle.setproctitle(THREADNAME)	
				except:
					pass
			except:
				OK_PRE_OPT_PULL = 0
			#
			if OK_PRE_OPT_PULL == 1:
			# PN ------------------ BEGIN GUTS_OF_ROUTINE ------------------- END PN
				# CONNECT TO THE MySQL DATABASE
				try:
					# DEFINE WHAT IS USED AS A SPLITTE FOR MySQL PUSHES
					#   THIS IS ALWAYS A COMMA
					splitter = str(',')
					# INITIALIZE DATA DUMP HOLDING REGISTER
					value_final = ''
					fire_up_sql()
					mysql_is_down = 0
				except:
					mysql_is_down = 1
				# PROCEED ONLY IF THE MySQL SERVER CAN BE CONTACTED
				if mysql_is_down != 1:
					# CONNECT TO THE TELNET DEVICE
					try:
						fire_up_telnet()
						telnet_is_down = 0
					except:
						telnet_is_down = 1
					# PROCEED ONLY IF THE DEVICE CAN BE CONTACTED
					while telnet_is_down != 1:
						try:	
							try:
								# -- READ EXPECT WITH A TIMEOUT
								RAWINPUT = tn.expect([YOURENDOFLINE],YOURTIMEOUT_INT)
								print "-- Value Incoming..."
								print " -- -- In RAW form..."
								print RAWINPUT
								INPUT1, INPUT2, INPUT3 = RAWINPUT
								print "-- -- In STRING form..."
								INPUT = str(RAWINPUT)
								INPUT1 = str(INPUT1)
								INPUT2 = str(INPUT2)
								INPUT3 = str(INPUT3)
								INPUT3 = INPUT3.replace(YOURENDOFLINE,'')
								print "-- -- -- INDEX: " + INPUT1
								print "-- -- -- MATCH: " + INPUT2
								print "-- -- -- VALUE: " + INPUT3
								if INPUT == 'EOFError':
									DROPPED = 1
									fault = "-- I/O miscommunication or Receive Error."
								else:
									if INPUT2 == 'None':
										DROPPED = 1
										fault = "-- Timeout, no data in " + YOURTIMEOUT + " seconds."
									else:
										DROPPED = 0
								if DROPPED == 0:
									INPUT_OUT = INPUT3[STARTCHAR:ENDCHAR]
									print "-- -- -- PARSED: " + INPUT_OUT
									print ""
									RECYCLE_COMM = 0
									# CHECK for NUMERIC VALUE
									if REQUIRENUMERICVALUE == 'yes':
										print "-- Checking for numeric data value..."
										try:
											TEST_NUMERIC = int(INPUT_OUT)
											print "-- -- data value IS numeric."
											print ""
											INPUT_OUT = int(INPUT_OUT)
										except:
											print "-- -- data value is NOT numeric."
											print "-- -- DISCARDING!"
											print ""
											DROPPED = 1
									else:
										print "-- Ignoring data type (string or numeric)..."
										print ""
								else:
									RECYCLE_COMM = 1
							except:
								INPUT_OUT = int(0)
								DROPPED = 1
								RECYCLE_COMM = 1
								fault = "-- Garbage Data Receive... Refreshing Connection."
							if DROPPED == 0:
								SEEK_N_DESTROY = 0
								# PULL THE ACTIVE EOR IN FROM THE SEER WARRIOR LaBLS EOR_TABLE
								comment_query = "SELECT * FROM " + EOR_TABLE + " WHERE LINE LIKE \'" + YOURDEVICENAMEFORLOG + "\'"
								comment_query = str(comment_query)
								print "Active LINE string incoming..."
	                                                        print comment_query
								sql_cursor.execute (comment_query)
								# COMMIT QUERY TO DB
								# -- PATCH FOR InnoDB ENGINE (and future MyISAM Engine)
								if COMMITTRANSACTIONS == "YES":
									try:
										# PUNCH THE CHANGE IN
										sql_connect.commit()
									except:
										# REVERT
										sql_connect.rollback()
								value_fetched = sql_cursor.fetchone()
								value_eor = value_fetched[1]
								value_eor = int(value_eor)
	                                                        print value_eor
								if value_eor == INPUT_OUT:
									# MATCH WAS FOUND
									SEEK_N_DESTROY = 1
									print ""
									print "-- end of run barcode detected, execute."
								else:
									# MATCH NOT FOUND
									print ""
									print "-- these are not the droids you are looking for."
								if SEEK_N_DESTROY == 1:
									# IF A MATCH IS FOUND, WRITE DECLARED VALUE TO TARGET OPC DEVICE
									# -- push via mod_openopc
									datestamp = datetime.now()
									datestamp_mysql = datestamp.strftime("%Y_%m%d_%H:%M:%S")
									datestamp = datestamp.strftime("%Y_%m%d_%H-%M-%S")
									FLATFILE = os.path.join(TEMPDIR, THREADNAME)
									FLATFILE = FLATFILE + "_" + datestamp + "_" + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + ".temp"
									print "-- built export file..."
									print FLATFILE
									FLATFILE_WORK = file(FLATFILE,'wt')
									FLATFILE_WORK = open(FLATFILE,'w')
									FLATFILE_CONTENT = "# START WRITE_DAEMON EVENT FILE FROM syphon.\n"
									FLATFILE_CONTENT = FLATFILE_CONTENT + "[your_write_type]\n"
									FLATFILE_CONTENT = FLATFILE_CONTENT + "YOURWRITETYPE:DECLARED\n"
									FLATFILE_CONTENT = FLATFILE_CONTENT + "# -- WRITE DECLARED VALUES TO OPC TARGET\n"
									FLATFILE_CONTENT = FLATFILE_CONTENT + "[your_leafers]\n"
									FLATFILE_CONTENT = FLATFILE_CONTENT + "YOURLEAFERS:"
									FLATFILE_CONTENT = FLATFILE_CONTENT + "XXX" + YOURTARGET + "YYY" + YOURLEAF + "&" + YOUREXECUTIONVALUE + "&|" + "\n"
									FLATFILE_CONTENT = FLATFILE_CONTENT + "YOURWRITEPRESET:NONE\n"
									FLATFILE_CONTENT = FLATFILE_CONTENT + "# -- NAME OF PRESET FILE TO WRITE\n"
									FLATFILE_CONTENT = FLATFILE_CONTENT + "# END OF FILE\n"
									FLATFILE_WORK.write(FLATFILE_CONTENT)
									FLATFILE_WORK.close()
									# MOVE THE TEMP FILE TO THE DAEMON IMPORT DIRECTORY
									EXPORT = os.path.join(PROGPATH_MODOPENOPC_GWCOMM, YOURMODOPENOPCDAEMON)
									EXPORT = os.path.join(EXPORT, THREADNAME)
									EXPORT = EXPORT + "_" + datestamp + "_" + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + ".event"
									shutil.move(FLATFILE,EXPORT)
									print "-- handed the file off to mod_openopc..."
									# LOG THE ACTION
									comment_query = "We searched for EOR barcode id " + str(value_eor) + " ----- found it as " + str(INPUT3) + " at " + str(datestamp) + "."
									comment_query = "INSERT INTO " + ACTION_TABLE + " VALUES (\'" + datestamp_mysql + "\', \'" + YOURDEVICENAMEFORLOG + "\', \'automatic\', \'SYS_EOR_EXEC\', \'" + comment_query + "\')"
									comment_query = str(comment_query)
									sql_cursor.execute (comment_query)
								else:
									pass
							else:
								print "-- not exporting anything..."
							datestamp = datetime.now()
							datestamp = datestamp.strftime("%Y_%m%d_%H:%M:%S")
							if RECYCLE_COMM == 1:
								# KEEP ALIVE FUNCTION
								print ""
								print "Executing MySQL 'keep-alive' instructions..."
								syphon_fault_recycle()
								RECYCLE_COMM = 0
								print "Awaiting input on..."
								datestamp = datetime.now()
								datestamp = datestamp.strftime("%Y_%m%d_%H-%M-%S")
								print YOURDEVICENAME + " at " + datestamp
							else:
								print ""
								print "Awaiting next input on..."
								print YOURDEVICENAME + " at " + datestamp
								print ""
						# END KEEP RUNNING UNTIL WE HAVE A PROBLEM
						except:
							syphon_fault_recycle()
					# END PROCEED ONLY IF THE TELNET DEVICE CAN BE CONTACTED
					else:
						syphon_error_communication()
				# END PROCEED ONLY IF THE MySQL SERVER CAN BE CONTACTED
				else:
					syphon_error_sql()
				# CLOSE CONNECTION TO MySQL DB
				try:
					sql_cursor.close ()
					sql_connect.close ()
				except:
					syphon_error_sql_close()
			# PN ------------------ END GUTS_OF_ROUTINE --------------------- END PN
			else:
				syphon_error_options()
		else:
			syphon_error_command()
	else:
		print ""
		print "SKIPPING RUN_SEER_WARRIOR_EOR_EXECUTE ..."
#
#
# RUN_MYSQL
	if YOURCOMMAND1 == 'RUN_MYSQL':
		print ""
		print "STARTING ROUTINE - RUN_MYSQL"
		if OK_RUN_MYSQL >= 1:
		# -- RUN_MYSQL
		# -- -- A ROUTINE TO READ TELNET DATA LINE BY LINE AND
		# -- -- THEN PUSH THAT DATA OUT TO A MySQL DATABASE
		# -- -- WITH SOURCE ID AND DATESTAMP.
		# -- -- YOURCOMMAND1 	... RUN_MYSQL
		# -- -- YOUROPTION1	... PRESET FILE NAME wo EXTENSION
		# -- -- YOUROPTION2	... CONDITIONAL | (blank)
			#
			# SCAN ALL PRESETS AND OPTIONS
			try:
				pull_in_preset()
				# DECLARE THAT WE HAVE ACHIEVED A GOOD PRESET AND OPTIONS PULL
				OK_PRE_OPT_PULL = 1
				# NAME THIS THREAD
				THREADNAME = "syphon_RUN_MYSQL_" + YOURDEVICENAME
				try:
					setproctitle.setproctitle(THREADNAME)	
				except:
					pass
			except:
				OK_PRE_OPT_PULL = 0
			#
			if OK_PRE_OPT_PULL == 1:
			# PN ------------------ BEGIN GUTS_OF_ROUTINE ------------------- END PN
				# CONNECT TO THE MySQL DATABASE
				try:
					# DEFINE WHAT IS USED AS A SPLITTER FOR MySQL PUSHES
					#   THIS IS ALWAYS A COMMA
					splitter = str(',')
					# INITIALIZE DATA DUMP HOLDING REGISTER
					value_final = ''
					fire_up_sql()
					mysql_is_down = 0
				except:
					mysql_is_down = 1
				# PROCEED ONLY IF THE MySQL SERVER CAN BE CONTACTED
				if mysql_is_down != 1:
					# CONNECT TO THE TELNET DEVICE
					try:
						fire_up_telnet()
						telnet_is_down = 0
					except:
						telnet_is_down = 1
					# PROCEED ONLY IF THE DEVICE CAN BE CONTACTED
					while telnet_is_down != 1:
						try:	
							try:
								# -- READ EXPECT WITH A TIMEOUT
								RAWINPUT = tn.expect([YOURENDOFLINE],YOURTIMEOUT_INT)
								print "-- Value Incoming..."
								print " -- -- In RAW form..."
								print RAWINPUT
								INPUT1, INPUT2, INPUT3 = RAWINPUT
								print "-- -- In STRING form..."
								INPUT = str(RAWINPUT)
								INPUT1 = str(INPUT1)
								INPUT2 = str(INPUT2)
								INPUT3 = str(INPUT3)
								INPUT3 = INPUT3.replace(YOURENDOFLINE,'')
								print "-- -- -- INDEX: " + INPUT1
								print "-- -- -- MATCH: " + INPUT2
								print "-- -- -- VALUE: " + INPUT3
								if INPUT == 'EOFError':
									DROPPED = 1
									fault = "-- I/O miscommunication or Receive Error."
								else:
									if INPUT2 == 'None':
										DROPPED = 1
										fault = "-- Timeout, no data in " + YOURTIMEOUT + " seconds."
									else:
										DROPPED = 0
								if DROPPED == 0:
									INPUT_OUT = INPUT3[STARTCHAR:ENDCHAR]
									print "-- -- -- PARSED: " + INPUT_OUT
									print ""
									RECYCLE_COMM = 0
									# CHECK for NUMERIC VALUE
									if REQUIRENUMERICVALUE == 'yes':
										print "-- Checking for numeric data value..."
										try:
											TEST_NUMERIC = float(INPUT_OUT)
											print "-- -- data value IS numeric."
											print ""
											INPUT_OUT = float(INPUT_OUT)
											INPUT_OUT = str(INPUT_OUT)
										except:
											print "-- -- data value is NOT numeric."
											print "-- -- DISCARDING!"
											print ""
											DROPPED = 1
									else:
										print "-- Ignoring data type (string or numeric)..."
										print ""
									# PERFORM CONDITIONAL QUERY AND CHECK FOR CONDITIONAL MATCH
									if YOUROPTION2 == 'CONDITIONAL':
										print "-- Checking for condition required to handle data value..."
										trigger_query = "SELECT * FROM " + YOURDEVICETABLENAME + " WHERE " + YOURDEVICECOLUMNNAME + " LIKE \'" + YOURDEVICENAMEFORLOG + "\' ORDER BY DATESTAMP DESC LIMIT 1"
										trigger_query = str(trigger_query)
										print "-- -- Conditional value to test, incoming..."
										print trigger_query
										sql_cursor.execute (trigger_query)
										# COMMIT QUERY TO DB
										# -- PATCH FOR InnoDB ENGINE (and future MyISAM Engine)
										if COMMITTRANSACTIONS == "YES":
											try:
												# PUNCH THE CHANGE IN
												sql_connect.commit()
											except:
												# REVERT
												sql_connect.rollback()
										value_trigger = sql_cursor.fetchone()
										value_trigger = value_trigger[2]
										value_trigger = str(value_trigger)
										print value_trigger
										print "-- Checking for conditional match data value... (" + str(YOURCONDITIONALVALUE) + " =?= " + str(value_trigger) + ")"
										if str(YOURCONDITIONALVALUE) == str(value_trigger):
											print "-- -- match FOUND!"
											print ""
										else:
											print "-- -- match NOT found."
											print "-- -- DISCARDING!"
											print ""
											DROPPED = 1
								else:
									RECYCLE_COMM = 1
							except:
								INPUT_OUT = int(0)
								DROPPED = 1
								RECYCLE_COMM = 1
								fault = "-- Garbage Data Receive... Refreshing Connection."
							if DROPPED == 0:
								# IF INPUT IS NOT BAD THEN PUSH IT TO MySQL DATABASE TABLE
								datestamp = datetime.now()
								datestamp = datestamp.strftime("%Y_%m%d_%H:%M:%S")
								# CAST AS STRING
								INPUT_OUT = str(INPUT_OUT)
								# ASSEMBLE THE FINAL VALUE FOR EXPORT (ALL FIELDS OF CHECKWEIGHER TABLE [DATA TABLE])
								value_final = "\'" + datestamp + "\'" + splitter + "\'" + YOURDEVICENAMEFORLOG + "\'" + splitter + "\'" + INPUT_OUT + "\'"
								# PUSH THE ROW INTO THE DATABASE
								# -- psuedo_query_example = INSERT INTO SQL_TABLE VALUES(value_final)
								sql_query = "INSERT INTO " + TABLE_SYPHON + " VALUES(" + value_final + ")"
								print ""
								print "NOTICE! -- EXPORTING RESULTS TO YOUR SQL TABLE - FOR..." + YOURDEVICENAMEFORLOG
								print "WE ARE USING THE FOLLOWING QUERY STRING..."
								print sql_query
								sql_query = str(sql_query)
								sql_cursor.execute (sql_query)
								# COMMIT QUERY TO DB
								# -- PATCH FOR InnoDB ENGINE (and future MyISAM Engine)
								if COMMITTRANSACTIONS == "YES":
									try:
										# PUNCH THE CHANGE IN
										sql_connect.commit()
									except:
										# REVERT
										sql_connect.rollback()
								# END PUSH THE ROW INTO THE DATABASE
								value_final = ''
							else:
								print "-- not exporting anything..."
							datestamp = datetime.now()
							datestamp = datestamp.strftime("%Y_%m%d_%H:%M:%S")
							if RECYCLE_COMM == 1:
								# KEEP ALIVE FUNCTION
								print ""
								print "Executing 'keep-alive' instructions..."
								syphon_fault_recycle()
								print "Awaiting input on..."
								datestamp = datetime.now()
								datestamp = datestamp.strftime("%Y_%m%d_%H-%M-%S")
								print YOURDEVICENAME + " at " + datestamp
							else:
								print ""
								print "Awaiting next input on..."
								print YOURDEVICENAME + " at " + datestamp
								print ""
						# END KEEP RUNNING UNTIL WE HAVE A PROBLEM
						except:
							syphon_fault_recycle()
					# END PROCEED ONLY IF THE TELNET DEVICE CAN BE CONTACTED
					else:
						syphon_error_communication()
				# END PROCEED ONLY IF THE MySQL SERVER CAN BE CONTACTED
				else:
					syphon_error_sql()
				# CLOSE CONNECTION TO MySQL DB
				try:
					sql_cursor.close ()
					sql_connect.close ()
				except:
					syphon_error_sql_close()

			# PN ------------------ END GUTS_OF_ROUTINE --------------------- END PN
			else:
				syphon_error_options()
		else:
			syphon_error_command()
	else:
		print ""
		print "SKIPPING RUN_MYSQL ..."
#
#
# TEST_COMM
	if YOURCOMMAND1 == 'TEST_COMM':
		print ""
		print "STARTING ROUTINE - TEST_COMM"
		if OK_TEST_COMM >= 2:
		# -- TEST_COMM
		# -- -- A ROUTINE TO READ TELNET DATA IN TEST MODE
		# -- -- YOURCOMMAND1 	... TEST_COMM
		# -- -- YOUROPTION1	... IP ADDRESS OF TEST DEVICE
		# -- -- YOUROPTION2	... PORT OF TEST DEVICE
		# -- -- YOUROPTION3	... END OF LINE TO SEARCH FOR (OPTIONAL)
		# -- -- YOUROPTION4	... TIMEOUT (OPTIONAL - DEFAULT TO 180 sec)
			#
			# SETUP
			try:
				THREADNAME = "syphon_TEST_COMM"
				try:
					setproctitle.setproctitle(THREADNAME)	
				except:
					pass
				YOURDEVICEIP = YOUROPTION1
				YOURDEVICEPORT = YOUROPTION2
				if YOUROPTION3 == 'null':
					SKIPEOL = 1
					YOUREOL = '\r'
				else:
					YOUREOL = YOUROPTION3
					SKIPEOL = 0
				if YOUROPTION4 != 'null':
					YOURTIMEOUT = int(YOUROPTION4)
				else:
					YOURTIMEOUT = 180
				OK_PRE_OPT_PULL = 1
			except:
				OK_PRE_OPT_PULL = 0
			#
			if OK_PRE_OPT_PULL == 1:
			# PN ------------------ BEGIN GUTS_OF_TEST_COMM ------------------- END PN
				# CONNECT TO THE TELNET DEVICE
				try:
					fire_up_telnet()
					telnet_is_down = 0
				except:
					telnet_is_down = 1
				# PROCEED ONLY IF THE DEVICE CAN BE CONTACTED
				while telnet_is_down != 1:
					try:	
						if SKIPEOL == 0:
							time.sleep(0)
						else:
							time.sleep(2)
						# -- READ EXPECT
						RAWINPUT = tn.expect([YOUREOL],YOURTIMEOUT)
						print "-- Value Incoming..."
						print " -- -- In RAW form..."
						print RAWINPUT
						try:
							INPUT1, INPUT2, INPUT3 = RAWINPUT
							print "-- -- In STRING form..."
							INPUT1 = str(INPUT1)
							INPUT2 = str(INPUT2)
							INPUT3 = str(INPUT3)
							print "-- -- -- INDEX: " + INPUT1
							print "-- -- -- MATCH: " + INPUT2
							print "-- -- -- VALUE: " + INPUT3
							print ""
						except:
							INPUT = 0
							print "-- Garbage data on the line."
							print ""
					# END KEEP RUNNING UNTIL WE HAVE A PROBLEM
					except:
						syphon_fault_recycle()
				# END PROCEED ONLY IF THE TELNET DEVICE CAN BE CONTACTED
				else:
					syphon_error_communication()
			# PN ------------------ END GUTS_OF_TEST_COMM --------------------- END PN
			else:
				syphon_error_options()
		else:
			syphon_error_command()
	else:
		print ""
		print "SKIPPING TEST_COMM ..."
#
# AUTO_LAUNCH
	if YOURCOMMAND1 == 'AUTO_LAUNCH':
		print ""
		print "STARTING ROUTINE - AUTO_LAUNCH"
		if OK_AUTO_LAUNCH == 1:
		# -- AUTO_LAUNCH
		# -- -- A ROUTINE TO AUTO LAUNCH YOUR PRESET SUBROUTINES,
		# -- -- BASED ON YOUR ENTRY IN THE GLOBAL OPTIONS FILE.
		# -- -- YOURCOMMAND1 	... AUTO_LAUNCH
		# -- -- YOUROPTION1	... CONFIRM (anything else just prints help)
			# NAME THIS THREAD
			if YOUROPTION1 == 'CONFIRM':
				THREADNAME = "syphon_" + YOURCOMMAND1 + "_" + YOUROPTION1
			else:
				THREADNAME = "syphon_" + YOURCOMMAND1 + "_" + "VOID"
			try:
				setproctitle.setproctitle(THREADNAME)
			except:
				pass
			#
			# PN ------------------ BEGIN GUTS_OF_AUTO_LAUNCH ----------------- END PN
			print ""
			print "NOTICE! -- SUCCESSFULLY ENTERED THE AUTO_LAUNCH ROUTINE"
			# WAIT FOR MOD_OPENOPC OR ANY OTHER PRE REQUISITES TO HAVE BEEN LOADED
			print "-- waiting 120 seconds to allow pre-req's to load..."
			dumb_waiter = 120
			while dumb_waiter > 0:
				time.sleep(10)
				dumb_waiter = dumb_waiter - 10
				print "-- " + str(dumb_waiter) + " seconds"
			print "-- ready!"
			# FIRST TIME THROUGH ROUTINE?
			dumb_waiter_first = 1
			AUTO_LAUNCH_PROCESS_MONITOR = []
			# RUN ROUTINE UNLESS FAULT
			try:
				# RUN INDEFINATELY
				while True:
					# CYCLE THROUGH ALL PRESETS LISTED IN GLOBAL OPTIONS FILE
					# -- PERFORM SAME LAUNCH (FORK) FOR ALL
					AUTO_LAUNCH_INDEX_INTEGER = 0
					for AUTO_LAUNCH_INDEX in range(len(AUTO_LAUNCH)):
						print ""
						print "-- WORKING WITH PRESET IDENTIFIED AS..."
						print AUTO_LAUNCH[AUTO_LAUNCH_INDEX]
						AUTO_LAUNCH_COMMAND_PARTS = AUTO_LAUNCH[AUTO_LAUNCH_INDEX]
						AUTO_LAUNCH_COMMAND_PARTS = AUTO_LAUNCH_COMMAND_PARTS.split(',')
						AUTO_LAUNCH_COMMAND = [PYTHON_EXECUTABLE,SYPHON_EXECUTABLE]
						AUTO_LAUNCH_PROCESS = "syphon_" + AUTO_LAUNCH_COMMAND_PARTS[0] + "_" + AUTO_LAUNCH_COMMAND_PARTS[1];
						for AUTO_LAUNCH_COMMAND_PARTS_INDEX in range(len(AUTO_LAUNCH_COMMAND_PARTS)):
							AUTO_LAUNCH_COMMAND.append(AUTO_LAUNCH_COMMAND_PARTS[AUTO_LAUNCH_COMMAND_PARTS_INDEX])
						if dumb_waiter_first == 1:
							print "-- -- ATTEMPTING SPAWN..."
							print AUTO_LAUNCH_PROCESS
							try:
								AUTO_LAUNCH_PROCESS_MONITOR.insert(AUTO_LAUNCH_INDEX_INTEGER,subprocess.Popen(AUTO_LAUNCH_COMMAND))
								print "-- -- -- SUCCESSFUL LAUNCH."
								time.sleep(0.5)
							except:
								print "-- -- -- FATAL ERROR !"
								print "-- -- -- UNABLE TO EXECUTE LAUNCH."
						else:
							print "-- -- VERIFYING LAUNCHED PROCESS'S PERSISTENCE..."
							print AUTO_LAUNCH_PROCESS
							try:
								AUTO_LAUNCH_PROCESS_PERSISTENCE = AUTO_LAUNCH_PROCESS_MONITOR[AUTO_LAUNCH_INDEX_INTEGER].poll()
								if AUTO_LAUNCH_PROCESS_PERSISTENCE:
									print "-- -- -- ERROR !"
									print "-- -- -- PROCESS HAS FAILED, RE-LAUNCHING."
									AUTO_LAUNCH_PROCESS_MONITOR[AUTO_LAUNCH_INDEX_INTEGER].wait()
									AUTO_LAUNCH_PROCESS_MONITOR[AUTO_LAUNCH_INDEX_INTEGER] = "x"
									time.sleep(3)
									AUTO_LAUNCH_PROCESS_MONITOR[AUTO_LAUNCH_INDEX_INTEGER] = subprocess.Popen(AUTO_LAUNCH_COMMAND)
									print "-- -- -- -- SUCCESSFULLY RE-LAUNCHED."
									time.sleep(0.5)
								else:
									print "-- -- -- VERIFIED."
							except:
								print "-- -- -- FATAL ERROR !"
								print "-- -- -- COULD NOT VERIFY -NOR- RE-LAUNCH PROCESS."
						AUTO_LAUNCH_INDEX_INTEGER = AUTO_LAUNCH_INDEX_INTEGER + 1
					# UNSET FIRST TIME THROUGH ROUTINE
					dumb_waiter_first = 0
					# RECYCLE DELAY
					print ""
					print "-- waiting 5 seconds before next verification of process persistence..."
					time.sleep(5)
					print ""
			# FAULT
			except:
				syphon_error_autolaunch()
			# HOLD A FEW SECONDS TO USERS CAN SEE INFO ON SCREEN
			time.sleep(5)
		# PN ------------------ END GUTS_OF_AUTO_LAUNCH ------------------- END PN
		else:
			syphon_error_command()
	else:
		print ""
		print "SKIPPING AUTO_LAUNCH ..."
#
#
# PN ------------------ END OK_GLOBAL_OPTS CONDITIONAL ------- END PN
else:
	syphon_error_global_options()
#
# HELP
if YOURCOMMAND1 == 'HELP':
	# NAME THIS THREAD
	THREADNAME = "syphon_" + YOURCOMMAND1
	try:
		setproctitle.setproctitle(THREADNAME)	
	except:
		pass
	print ""
	print "STARTING ROUTINE - HELP"
	# PN ------------------ START GUTS_OF_HELP --------------- END PN
	print ""
	print "Welcome to syphon."
	print "------------------------------------------------------------"
	print ""
	print "This project has been based on 'the blips', the proof"
	print "of concept, barcode label identified package sorter."
	print ""
	print "OPC functionality requires you have already installed"
	print "mod_openopc, and have running an active WRITE_DAEMON."
	print ""
	print "Take your time, and due diligence prior to setting up "
	print "a syphon routine... it will do you much better"
	print "to properly set this program up prior to running it,"
	print "because the consequences of writing improper values"
	print "to what may be your mission critical OPC devices, or"
	print "worse, corrupting those devices, is very possible..."
	print ""
	print "BASIC USAGE..."
	print "------------------------------------------------------------"
	print ""
	print "/path/to/python /opt/syphon/prog/syphon.py [ARGS]"
	print ""
	print "ARGUMENTS..."
	print "------------------------------------------------------------"
	print ""
	print "syphon.py RUN_OPC [preset_file] [LOG | (blank)] [CONDITIONAL | (blank)]"
	print "-- -- Connect to the device indicated by the preset_file,"
	print "-- -- and sit on the connection to receive data.  Upon"
	print "-- -- receipt, export data to mod_openopc for immediate"
	print "-- -- writing to the OPC device indicated by the preset_file."
	print ""
	print "syphon.py RUN_MATCH [preset_file] [SEARCH | (blank)] [LOG | (blank)] [CONDITIONAL | (blank)] "
	print "-- -- Connect to the device indicated by the preset file,"
	print "-- -- and sit on the connection to receive data.  Upon"
	print "-- -- receipt, compare the data to a pre-declared value, and"
	print "-- -- if it is a match, then export a declared value to "
	print "-- -- mod_openopc for immediate writing to the OPC device"
	print "-- -- indicated by the preset_file."
	print ""
	print "syphon.py RUN_CONDITIONAL_RESTRANSMIT [preset_file]"
	print "-- -- Connect to the device indicated by the preset file,"
	print "-- -- after a second client has connected to syphon.  Then,"
	print "-- -- sit on the connection to recevive data.  Upon receipt,"
	print "-- -- check for a database flag (value) to decide whether "
	print "-- -- we should retransmit the value to the second client,"
	print "-- -- on the port indicated by the preset file."
	print "-- -- USES BLOCKING IO - only one secondary client per"
	print "-- -- instance!"
	print ""
	print "syphon.py RUN_SEER_CHECKWEIGHERMODEL_V1 [preset_file]"
	print "-- -- A -custom- subroutine written for integration with the"
	print "-- -- S.E.E.R. CheckWeigher Model (v1-Eudamidas) which accepts"
	print "-- -- scale data (weights), and logs them to a MySQL database"
	print "-- -- along with the date / time, machine (preset) name, and"
	print "-- -- the current running machine recipe (as indicated by the"
	print "-- -- S.E.E.R. database table for CheckWeigher Model active"
	print "-- -- syphon recipes)."
	print "-- -- NOTE - this REQUIRES that you have already installed SEER"
	print "-- -- -- and the CHECKWEIGHERMODEL, that you have created"
	print "-- -- -- the appropriate SEER config files (global options and"
	print "-- -- -- local options files), and that you have populated the"
	print "-- -- -- 'SYPHON_table' prior to running this command in syphon."
	print ""
	print "syphon.py RUN_SEER_CHECKWEIGHERMODEL_V2 [preset_file]"
	print "-- -- A -custom- subroutine written for integration with the"
	print "-- -- S.E.E.R. CheckWeigher Model (v2-Leda) which functions"
	print "-- -- precisely the same as the CHECKWEIGHERMODEL_V1 subroutine,"
	print "-- -- with the added feature of logging the machine operator"
	print "-- -- as well."
	print ""
	print "syphon.py RUN_SEER_WARRIOR_EOR_ACQUIRE [preset_file]"
	print "-- -- A -custom- subroutine written for integration with the"
	print "-- -- S.E.E.R. Warrior Module's 'lactalis_bartender_labeling_system'"
	print "-- -- plugin."
	print "-- -- Logs the last scanned barcode from a device by updating a field"
	print "-- -- in a declared MySQL DB with the barcode value."
	print "-- -- NOTE - this REQUIRES that you have already installed SEER"
	print "-- -- -- and the WARRIOR MODULE, that you have created"
	print "-- -- -- the appropriate SEER config files (global options and"
	print "-- -- -- local options files), installed and configured the"
	print "-- -- -- proprietary 'lactalis_bartender_labeling_system' plugin,"
	print "-- -- -- and populated tables for the plugin prior to running"
	print "-- -- -- this command in syphon."
	print ""
	print "syphon.py RUN_SEER_WARRIOR_EOR_EXECUTE [preset_file]"
	print "-- -- A -custom- subroutine written for integration with the"
	print "-- -- S.E.E.R. Warrior Module's 'lactalis_bartender_labeling_system'"
	print "-- -- plugin."
	print "-- -- Scans a barcode from a device, compares it with a value stored"
	print "-- -- by the EOR_ACQUIRE subroutine in a MySQL database, and upon"
	print "-- -- finding a match, writes a declared value to a declared OPC"
	print "-- -- target device."
	print "-- -- NOTE - this REQUIRES that you have already installed SEER"
	print "-- -- -- and the WARRIOR MODULE, that you have created"
	print "-- -- -- the appropriate SEER config files (global options and"
	print "-- -- -- local options files), installed and configured the"
	print "-- -- -- proprietary 'lactalis_bartender_labeling_system' plugin,"
	print "-- -- -- and populated tables for the plugin prior to running"
	print "-- -- -- this command in syphon."
	print ""
	print "syphon.py RUN_MYSQL [preset_file] [CONDITIONAL | (blank)]"
	print "-- -- Connect to the device indicated by the preset_file,"
	print "-- -- and sit on the connection to receive data.  Upon"
	print "-- -- receipt, export data to mysql database, with datestamp"
	print "-- -- and data source identification."
	print ""
	print "syphon.py TEST_COMM [device_ip_address] [device_port]"
	print "      [EOL to search (optional)] [timeout (optional, 180]"
	print "-- -- Connect to the device indicated by the arguments,"
	print "-- -- but only accept the first input string.  This allows"
	print "-- -- us to effectively test communication."
	print ""
	print "syphon.py AUTO_LAUNCH CONFIRM"
	print "-- -- auto launches all subroutines or syphon commands"
	print "-- -- which are defined to auto launch in the global options"
	print "-- -- file."
	print "-- -- this is a great command to use at system startup,"
	print "-- -- rather than calling all of your presets individually."
	print "-- -- you should still test your individual presets first by"
	print "-- -- running them individually, so you can observe their"
	print "-- -- output in verbose mode... the auto launcher hides all"
	print "-- -- output in the background."
	print "-- -- the CONFIRM argument is required, anything else"
	print "-- -- will simply display a the items listed to auto launch"
	print "-- -- along with the help-file, but not actually launch them."
	print "-- -- NOTE!"
	print "-- -- -- Unix flavors should call AUTO_LAUNCH as follows..."
	print "-- -- -- [path-to]/nohup [path-to]/python [path-to]syphon.py AUTO_LAUNCH CONFIRM 2>/dev/null 1>/dev/null &"
	print "-- -- -- The above is recommend for use in your 'rc.local' or"
	print "-- -- -- startup file."
	print ""
	print "syphon.py HELP"
	print "-- -- Brings you here, to the help screen."
	print ""
	print "NOTICE -- THIS WINDOW WILL STAY VISIBLE FOR 90 SECONDS"
	print "OR UNTIL YOU CLOSE IT."
	print "------------------------------------------------------------"
	time.sleep(90)		
	# PN ------------------ END GUTS_OF_HELP ----------------- END PN
else:
	print ""
	print "SKIPPING HELP ..."
# 
# --------------------- CLEAN EXIT ----------------------------------
#exit()

