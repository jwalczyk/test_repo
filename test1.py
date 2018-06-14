def _ci_server_gitlab(body, toolchainId):

    event = request.headers.get('X-GitLab-Event')
    rc = _check_event(event, "Merge Request Hook")
    if rc is not None:
        return rc

    # For ping requests, gitlab simply doesn't append the action
    rc = _check_action(body['object_attributes'].get('action', 'Testing'))
    if rc is not None:
        return rc

    url_split = body['project']['web_url'].split('/')
    repo = url_split[4].replace('.git', '')
    owner = url_split[3]

    statuses_url = '/'.join([
        url_split[0],
        url_split[1],
        url_split[2],
        'api/v4/projects',
        owner + '%2F' + repo,
        'statuses',
        body['object_attributes']['last_commit']['id']])

    project, sources, rc = _get_sources(toolchainId)
    if sources is None:
        return rc

    doi_callback_base, rc = _get_doi_callback_base()
    if doi_callback_base is None:
        return rc

    pull_id = body['object_attributes']['iid']

