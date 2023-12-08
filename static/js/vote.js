//Updates the Arrow visuals on the screen
const voteContainers = document.querySelectorAll(".vote");

voteContainers.forEach(container => {
    const upVoteButton = container.querySelector('.upvote-button');
    const downVoteButton = container.querySelector('.downvote-button');
    const points = container.querySelector('.points');
    let hasUpVoted = false;
    let hasDownVoted = false;

    upVoteButton.addEventListener('click', function () {
        if (hasDownVoted) {
            points.textContent = parseInt(points.textContent) + 1;
            downVoteButton.disabled = false;
            upVoteButton.disabled = false;
            hasUpVoted = false;
            hasDownVoted = false;
        } else if (!hasUpVoted) {
            points.textContent = parseInt(points.textContent) + 1;
            upVoteButton.disabled = true;
            downVoteButton.disabled = false;
            hasUpVoted = true;
            hasDownVoted = false;
        }
    });

    downVoteButton.addEventListener('click', function () {
        if (hasUpVoted) {
            points.textContent = parseInt(points.textContent) - 1;
            upVoteButton.disabled = false;
            downVoteButton.disabled = false;
            hasUpVoted = false;
            hasDownVoted = false;
        } else if (!hasDownVoted) {
            points.textContent = parseInt(points.textContent) - 1;
            downVoteButton.disabled = true;
            upVoteButton.disabled = false;
            hasDownVoted = true;
            hasUpVoted = false;
        }
    });
});
