class Comment:
    def __init__(self, submitter, upvotes, downvotes, id, content):
        self.submitter = submitter #user object
        self.upvotes = upvotes #list of vote objects
        self.downvotes = downvotes #list of vote object 
        self.id = id
        self.content = content

    def net_upvotes(self):
        return len(self.upvotes) - len(self.downvotes)
