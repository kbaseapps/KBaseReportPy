/*
 * Workspace types for report data that gets generated and saved on report creation.
 * These objects are generated in this module as result data from the create()
 * and create_extended_report() methods found in KBaseReport.spec
 */
module KBaseReport {
    /*
     * Workspace ID reference in the format 'workspace_id/object_id/version'
     * @id ws
     */
    typedef string ws_id;

    /*
     * Reference to a handle ID
     * @id handle
     */
    typedef string handle_ref;

    /*
     * Represents a Workspace object with some brief description text
     * that can be associated with the object.
     * Required arguments:
     *     ws_id ref - workspace ID in the format 'workspace_id/object_id/version'
     * Optional arguments:
     *     string description - A plaintext, human-readable description of the
     *         object created.
     * @optional description
     */
    typedef structure {
        ws_id ref;
        string description;
    } WorkspaceObject;

    /*
     * Represents a single file or zipped directory of files that the report
     * links to or renders as HTML. Used by Report for either html_links or file_links.
     * Required arguments:
     *     handle_ref handle - Handle ID
     *     string name - Plain-text name of the file (shown to the user)
     *     string URL - URL of shock node: <shock-url>/node/<shock-handle-id>
     * Optional arguments:
     *     string label - A plain-text, human-readable label for this file
     *     string description - A more detailed, human-readable description of the file
     * @optional description label
     */
    typedef structure {
        handle_ref handle;
        string description;
        string name;
        string label;
        string URL;
    } LinkedFile;

    /*
     * A Report of a method run in KBase. Both create() and
     * create_extended_report() from KBaseReport.spec ultimately generate these
     * objects and store them in the workspace.
     * Optional arguments:
     *     string text_message - Readable plain-text report message
     *     list<string> warnings - A list of plain-text warning messages
     *     list<WorkspaceObject> objects_created - List of result workspace objects that this app
     *         has created. They will get linked in the report view
     *     list<LinkedFile> file_links - List of LinkedFiles that the report
     *         lists out for the user to download
     *     list<LinkedFile> html_links - List of zipped directories of HTML
     *         files and content that the report will render or link for download
     *     string direct_html - Simple HTML text that will be rendered within the report widget.
     *         If you pass in both direct_html and html_links, then direct_html will be ignored
     *     int direct_html_link_index - Index in html_links to set the direct/default view in the
     *         report (ignored if direct_html is present)
     * @optional warnings file_links html_links direct_html direct_html_link_index
     * @metadata ws length(warnings) as Warnings
     * @metadata ws length(text_message) as Message Length
     * @metadata ws length(objects_created) as Objects Created
     */
    typedef structure {
        string text_message;
        list<string> warnings;
        list<WorkspaceObject> objects_created;
        list<LinkedFile> file_links;
        list<LinkedFile> html_links;
        string direct_html;
        int direct_html_link_index;
    } Report;
};
