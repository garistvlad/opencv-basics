#include <opencv2/opencv.hpp>
#include <iostream>

int main(int argc, char *argv[])
{
    if (argc != 2)
    {
        std::cout << "Usage: `./lesson01 <IMAGE_FILEPATH>`\n";
        return EXIT_FAILURE;
    }

    cv::Mat image;
    // read an Image:
    image = cv::imread(argv[1], cv::IMREAD_GRAYSCALE);
    if (!image.data)
    {
        std::cout << "Can't read an image\n";
        return EXIT_FAILURE;
    }

    // display in window
    cv::imshow("My-Super-Image", image);
    cv::waitKey(0);

    // delete all the windows created
    cv::destroyAllWindows();

    return EXIT_SUCCESS;
}