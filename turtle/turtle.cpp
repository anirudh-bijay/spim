#include <inttypes.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

#include "turtle.h"

static pid_t turtle_pid;
static int turtle_pipefd[2];

static int open_pipe(void)
{
    int ret = pipe(turtle_pipefd);

    if (ret == -1)
        perror("pipe");

    return ret;
}

static void init_turtle(void)
{
    // Replace stdin with the pipe read end.
    if (dup2(turtle_pipefd[0], STDIN_FILENO) == -1) {
        perror("dup2");
        exit(EXIT_FAILURE);
    }

    // Close the pipe write end.
    if (close(turtle_pipefd[1]) == -1) {
        perror("close");
        exit(EXIT_FAILURE);
    }

    execl("../turtle/spim_turtle.py", "spim_turtle.py", NULL);
    exit(EXIT_FAILURE);
}

int spawn_turtle(void)
{
    if (open_pipe() == -1)
        return -1;

    pid_t pid = fork();

    if (pid == -1) {
        perror("fork");
        return -1;
    }

    if (!pid) {
        // Child process
        init_turtle();
    } else {
        // Parent process
        turtle_pid = pid;
        
        // Close the pipe read end.
        if (close(turtle_pipefd[0]) == -1) {
            perror("close");
            return -1;
        }
    }

    return 0;
}

void turtle_fd(int32_t distance)
{
    char buf[1024];
    int len = sprintf(buf, "fd %" PRId32 "\n", distance);
    write(turtle_pipefd[1], buf, len);
}

void turtle_bk(int32_t distance)
{
    char buf[1024];
    int len = sprintf(buf, "bk %" PRId32 "\n", distance);
    write(turtle_pipefd[1], buf, len);
}

void turtle_lt(int32_t angle)
{
    char buf[1024];
    int len = sprintf(buf, "lt %" PRId32 "\n", angle);
    write(turtle_pipefd[1], buf, len);
}

void turtle_rt(int32_t angle)
{
    char buf[1024];
    int len = sprintf(buf, "rt %" PRId32 "\n", angle);
    write(turtle_pipefd[1], buf, len);
}

void turtle_goto(int32_t posx, int32_t posy)
{
    char buf[1024];
    int len = sprintf(buf, "goto %" PRId32 " %" PRId32 "\n", posx, posy);
    write(turtle_pipefd[1], buf, len);
}

void turtle_pu(void)
{
    write(turtle_pipefd[1], "pu\n", 3);
}

void turtle_pd(void)
{
    write(turtle_pipefd[1], "pd\n", 3);
}

void turtle_exit(void)
{
    if (turtle_pid) {
        write(turtle_pipefd[1], "exit\n", 5);
        close(turtle_pipefd[1]);
    }
}