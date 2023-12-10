function formatTimestamp(utcTimestamp) {
    const currentTime = new Date(); // User's local time
    const inputTime = new Date(utcTimestamp + 'Z'); // Treat the input as UTC by appending 'Z'

    const diffInSeconds = Math.floor((currentTime - inputTime) / 1000);

    const secondsPerMinute = 60;
    const secondsPerHour = 3600;
    const secondsPerDay = 86400;
    const secondsPerMonth = 2592000; // Approximation
    const secondsPerYear = 31536000; // Approximation

    if (diffInSeconds < secondsPerMinute) {
        return diffInSeconds === 1 ? '1 second ago' : diffInSeconds + ' seconds ago';
    } else if (diffInSeconds < secondsPerHour) {
        const minutes = Math.floor(diffInSeconds / secondsPerMinute);
        return minutes === 1 ? '1 minute ago' : minutes + ' minutes ago';
    } else if (diffInSeconds < secondsPerDay) {
        const hours = Math.floor(diffInSeconds / secondsPerHour);
        return hours === 1 ? '1 hour ago' : hours + ' hours ago';
    } else if (diffInSeconds < secondsPerMonth) {
        const days = Math.floor(diffInSeconds / secondsPerDay);
        return days === 1 ? '1 day ago' : days + ' days ago';
    } else if (diffInSeconds < secondsPerYear) {
        const months = Math.floor(diffInSeconds / secondsPerMonth);
        return months === 1 ? '1 month ago' : months + ' months ago';
    } else {
        const years = Math.floor(diffInSeconds / secondsPerYear);
        return years === 1 ? '1 year ago' : years + ' years ago';
    }
}