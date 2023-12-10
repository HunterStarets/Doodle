const voteContainers = document.querySelectorAll(".vote");

voteContainers.forEach(container => {
    const postId = container.getAttribute('data-post-id');
    const commentId = container.getAttribute('data-comment-id');
    const points = container.querySelector('.points');

    const upVoteButton = container.querySelector('.upvote-button');
    const downVoteButton = container.querySelector('.downvote-button');
    
    
    upVoteButton.addEventListener('click', async function () {
        let result;
        if(postId)
            result = await handlePostVote(postId, 'up');
        else{
            result = await handleCommentVote(commentId, 'up');
        }

        if(result){
            updateButtonState(result, upVoteButton, downVoteButton, points);
        }
    });

    downVoteButton.addEventListener('click', async function () {
        let result;
        if(postId)
            result = await handlePostVote(postId, 'down');
        else{
            result = await handleCommentVote(commentId, 'down');
        }

        if(result){
            updateButtonState(result, upVoteButton, downVoteButton, points);
        }
    });
});


async function handlePostVote(postId, voteType) {
    try {
        const response = await fetch('/vote/post', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                post_id: postId,
                vote_type: voteType
            })
        });

        const data = await response.json();
        //console.log(data)
        if (response.status === 201) { //vote created
            return { voted: voteType, status: response.status, netVotes: data.netVotes };
        } else if (response.status === 200) { //vote deleted
            return { voted: null, status: response.status, netVotes: data.netVotes  };
        } else {
            // errors
            return { error: data.error, status: response.status, netVotes: data.netVotes  };
        }
    } catch (error) {
        console.error('Error:', error);
        return { error: 'An error occurred', status: 500 };
    }
}

async function handleCommentVote(commentId, voteType) {
    try {
        const response = await fetch('/vote/comment', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                comment_id: commentId,
                vote_type: voteType
            })
        });

        const data = await response.json();
        //console.log(data)
        if (response.status === 201) { //vote created
            return { voted: voteType, status: response.status, netVotes: data.netVotes };
        } else if (response.status === 200) { //vote deleted
            return { voted: null, status: response.status, netVotes: data.netVotes  };
        } else {
            // errors
            return { error: data.error, status: response.status, netVotes: data.netVotes  };
        }
    } catch (error) {
        console.error('Error:', error);
        return { error: 'An error occurred', status: 500 };
    }
}

function updateButtonState(result, upVoteButton, downVoteButton, points) {
    if (result.status === 201 || result.status === 200) { // vote created or deleted
        const isUpvoted = result.voted === 'up';
        const isDownvoted = result.voted === 'down';
        
        points.textContent = result.netVotes
        upVoteButton.disabled = isUpvoted;
        downVoteButton.disabled = isDownvoted;

        upVoteButton.classList.toggle('active', isUpvoted);
        downVoteButton.classList.toggle('active', isDownvoted);
    } else {
        console.error('Error:', result.error);
    }
}
