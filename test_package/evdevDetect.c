#include <libevdev/libevdev.h>

#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <stdio.h>
#include <unistd.h>

int main() {
    int fd = open("/dev/input/event0", O_RDWR);

    struct libevdev *dev;
    int ret = libevdev_new_from_fd(fd, &dev);
    if (ret < 0) {
        close(fd);
        return 1;
    }

    const char *name = libevdev_get_name(dev);
    printf("Device name is %s\n", name);

    libevdev_free(dev);
    close(fd);

    return 0;
}
