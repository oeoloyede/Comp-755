#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/wait.h>

int main() {
    pid_t pid;
    
    // Create 10 child processes
    for (int i = 1; i <= 10; i++) {
        pid = fork();
        
        if (pid < 0) {
            perror("Fork failed");
            exit(1);
        } else if (pid == 0) {
            // Child process execution
            int sleep_ms = i + 10;
            
            // usleep takes microseconds, so multiply milliseconds by 1000
            usleep(sleep_ms * 1000);
            
            printf("Child %d (PID: %d) assigned sleep time: %d ms\n", i, getpid(), sleep_ms);
            exit(0);
        }
    }

    // Parent process execution
    int status;
    pid_t reaped_pid;
    
    // Wait for exactly 10 children to finish
    for (int i = 1; i <= 10; i++) {
        reaped_pid = wait(&status);
        if (reaped_pid > 0) {
            printf("Parent successfully reaped child PID: %d\n", reaped_pid);
        }
    }
    
    printf("Parent has reaped all children and is now exiting.\n");
    return 0;
}