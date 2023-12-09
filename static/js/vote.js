const voteContainers = document.querySelectorAll(".vote");
console.log("vote has run");

voteContainers.forEach(container => {
    const postId = container.getAttribute('data-post-id');
    const voterId = container.getAttribute('voter-id');
    const points = container.querySelector('.points');

    const upVoteButton = container.querySelector('.upvote-button');
    const downVoteButton = container.querySelector('.downvote-button');
    
    
    upVoteButton.addEventListener('click', async function () {
        const result = await handleVote(postId, 'up');
        //console.log(result);
        updateButtonState(result, upVoteButton, downVoteButton, points);
    });

    downVoteButton.addEventListener('click', async function () {
        const result = await handleVote(postId, 'down');
        //console.log(result);
        updateButtonState(result, upVoteButton, downVoteButton, points);
    });
});


async function handleVote(postId, voteType) {
    try {
        const response = await fetch('/vote', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                // Add other headers if required
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

function updateButtonState(result, upVoteButton, downVoteButton, points) {
    if (result.status === 201 || result.status === 200) { // vote created or deleted
        const isUpvoted = result.voted === 'up';
        const isDownvoted = result.voted === 'down';
        
        points.textContent = result.netVotes
        upVoteButton.disabled = isUpvoted;
        downVoteButton.disabled = isDownvoted;

        // Optionally, you can add/remove classes to visually indicate the state
        upVoteButton.classList.toggle('active', isUpvoted);
        downVoteButton.classList.toggle('active', isDownvoted);
    } else {
        console.error('Error:', result.error);
    }
}
