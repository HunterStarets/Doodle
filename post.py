class Post:
    def __init__(self, title, submitter, community, comments, upvotes, downvotes, id, content):
        self.title = title #string
        self.submitter = submitter #user object
        self.community = community #community object
        self.comments = comments #list of comment objects
        self.upvotes = upvotes #list of vote objects
        self.downvotes = downvotes #list of vote object 
        self.id = id
        self.content = content

    def net_upvotes(self):
        return len(self.upvotes) - len(self.downvotes)

    