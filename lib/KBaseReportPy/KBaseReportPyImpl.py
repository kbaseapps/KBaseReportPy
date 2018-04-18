# -*- coding: utf-8 -*-
#BEGIN_HEADER
from DataFileUtil.DataFileUtilClient import DataFileUtil
import utils.report_utils as report_utils
from utils.validation_utils import validate_simple_report_params, validate_extended_report_params
import os
#END_HEADER


class KBaseReportPy:
    '''
    Module Name:
    KBaseReportPy

    Module Description:
    Module for a simple WS data object report type.
    '''

    ######## WARNING FOR GEVENT USERS ####### noqa
    # Since asynchronous IO can lead to methods - even the same method -
    # interrupting each other, you must be *very* careful when using global
    # state. A method could easily clobber the state set by another while
    # the latter method is running.
    ######################################### noqa
    VERSION = "0.0.1"
    GIT_URL = "https://github.com/jayrbolton/KBaseReportPy"
    GIT_COMMIT_HASH = "9959ea5b4e2f9bd757dfb421cd3320d58b6d72c0"

    #BEGIN_CLASS_HEADER
    #END_CLASS_HEADER

    # config contains contents of config file in a hash or None if it couldn't
    # be found
    def __init__(self, config):
        #BEGIN_CONSTRUCTOR
        self.callback_url = os.environ['SDK_CALLBACK_URL']
        self.scratch = config['scratch']
        self.dfu = DataFileUtil(self.callback_url)
        #END_CONSTRUCTOR
        pass


    def create(self, ctx, params):
        """
        Create a KBaseReport with a brief summary of an App run.
        :param params: instance of type "CreateParams" (Provide the report
           information. Either workspace name or workspace id is required 
           The structure is: params = { report: { text_message: '', warnings:
           ['w1'], objects_created: [ { ref: 'ws/objid', description: '' }]
           }, workspace_name: 'ws' workspace_id: id }) -> structure:
           parameter "report" of type "Report" (A simple Report of a method
           run in KBase. It only provides for now a way to display a fixed
           width text output summary message, a list of warnings, and a list
           of objects created (each with descriptions). @optional warnings
           file_links html_links direct_html direct_html_link_index @metadata
           ws length(warnings) as Warnings @metadata ws length(text_message)
           as Size(characters) @metadata ws length(objects_created) as
           Objects Created) -> structure: parameter "text_message" of String,
           parameter "warnings" of list of String, parameter
           "objects_created" of list of type "WorkspaceObject" (Represents a
           Workspace object with some brief description text that can be
           associated with the object. @optional description) -> structure:
           parameter "ref" of type "ws_id" (@id ws), parameter "description"
           of String, parameter "file_links" of list of type "LinkedFile"
           (Represents a file or html archive that the report should like to
           @optional description label) -> structure: parameter "handle" of
           type "handle_ref" (Reference to a handle @id handle), parameter
           "description" of String, parameter "name" of String, parameter
           "label" of String, parameter "URL" of String, parameter
           "html_links" of list of type "LinkedFile" (Represents a file or
           html archive that the report should like to @optional description
           label) -> structure: parameter "handle" of type "handle_ref"
           (Reference to a handle @id handle), parameter "description" of
           String, parameter "name" of String, parameter "label" of String,
           parameter "URL" of String, parameter "direct_html" of String,
           parameter "direct_html_link_index" of Long, parameter
           "workspace_name" of String, parameter "workspace_id" of Long
        :returns: instance of type "ReportInfo" (The reference to the saved
           KBaseReport.  The structure is: reportInfo = { ref:
           'ws/objid/ver', name: 'myreport.2262323452' }) -> structure:
           parameter "ref" of type "ws_id" (@id ws), parameter "name" of
           String
        """
        # ctx is the context object
        # return variables are: info
        #BEGIN create
        # Validate params
        params = validate_simple_report_params(params)
        info = report_utils.create_report(ctx, params, self.dfu)
        #END create

        # At some point might do deeper type checking...
        if not isinstance(info, dict):
            raise ValueError('Method create return value ' +
                             'info is not type dict as required.')
        # return the results
        return [info]

    def create_extended_report(self, ctx, params):
        """
        A more complex function to create a report that enables the user to specify files and html view that the report should link to
        :param params: instance of type "CreateExtendedReportParams"
           (Parameters used to create a more complex report with file and
           html links The following arguments allow the user to specify the
           classical data fields in the report object: string message -
           simple text message to store in report object list
           <WorkspaceObject> objects_created; list <string> warnings - a list
           of warning messages in simple text The following argument allows
           the user to specify the location of html files/directories that
           the report widget will render <or> link to: list <fileRef>
           html_links - a list of paths or shock node IDs pointing to a
           single flat html file or to the top level directory of a website
           The report widget can render one html view directly. Set one of
           the following fields to decide which view to render: string
           direct_html - simple html text that will be rendered within the
           report widget int  direct_html_link_index - use this to specify
           the index of the page in html_links to view directly in the report
           widget (ignored if html_string is set) The following argument
           allows the user to specify the location of files that the report
           widget should link for download: list <fileRef> file_links - a
           list of paths or shock node IDs pointing to a single flat file The
           following parameters indicate where the report object should be
           saved in the workspace: string report_object_name - name to use
           for the report object (job ID is used if left unspecified)
           html_window_height - height of the html window in the narrative
           output widget summary_window_height - height of summary window in
           the narrative output widget One of the following: string
           workspace_name - name of workspace where object should be saved
           int workspace_id - id of workspace where object should be saved)
           -> structure: parameter "message" of String, parameter
           "objects_created" of list of type "WorkspaceObject" (Represents a
           Workspace object with some brief description text that can be
           associated with the object. @optional description) -> structure:
           parameter "ref" of type "ws_id" (@id ws), parameter "description"
           of String, parameter "warnings" of list of String, parameter
           "html_links" of list of type "File" -> structure: parameter "path"
           of String, parameter "shock_id" of String, parameter "name" of
           String, parameter "description" of String, parameter "direct_html"
           of String, parameter "direct_html_link_index" of Long, parameter
           "file_links" of list of type "File" -> structure: parameter "path"
           of String, parameter "shock_id" of String, parameter "name" of
           String, parameter "description" of String, parameter
           "report_object_name" of String, parameter "html_window_height" of
           Double, parameter "summary_window_height" of Double, parameter
           "workspace_name" of String, parameter "workspace_id" of Long
        :returns: instance of type "ReportInfo" (The reference to the saved
           KBaseReport.  The structure is: reportInfo = { ref:
           'ws/objid/ver', name: 'myreport.2262323452' }) -> structure:
           parameter "ref" of type "ws_id" (@id ws), parameter "name" of
           String
        """
        # ctx is the context object
        # return variables are: info
        #BEGIN create_extended_report
        params = validate_extended_report_params(params)
        info = report_utils.create_extended(ctx, params, self.dfu)
        #END create_extended_report

        # At some point might do deeper type checking...
        if not isinstance(info, dict):
            raise ValueError('Method create_extended_report return value ' +
                             'info is not type dict as required.')
        # return the results
        return [info]
    def status(self, ctx):
        #BEGIN_STATUS
        returnVal = {'state': "OK",
                     'message': "",
                     'version': self.VERSION,
                     'git_url': self.GIT_URL,
                     'git_commit_hash': self.GIT_COMMIT_HASH}
        #END_STATUS
        return [returnVal]
