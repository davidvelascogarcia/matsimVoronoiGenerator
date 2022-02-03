'''
  * ***************************************************************
  *      Program: MATSim Voronoi Generator
  *      Type: Python
  *      Author: David Velasco Garcia @davidvelascogarcia
  * ***************************************************************
'''

# Libraries
import os
os.environ["OPENCV_IO_MAX_IMAGE_PIXELS"] = pow(2,40).__str__()

import cv2
import datetime
from halo import Halo
import numpy as np
import platform


class MATSimVoronoiGenerator:

    # Function: Constructor
    def __init__(self):

        # Build Halo spinner
        self.systemResponse = Halo(spinner='dots')

    # Function: getSystemPlatform
    def getSystemPlatform(self):

        # Get system configuration
        print("\nDetecting system and release version ...\n")
        systemPlatform = platform.system()
        systemRelease = platform.release()

        print("**************************************************************************")
        print("Configuration detected:")
        print("**************************************************************************")
        print("\nPlatform:")
        print(systemPlatform)
        print("Release:")
        print(systemRelease)

        return systemPlatform, systemRelease

    # Function: getRootFiles
    def getRootFiles(self):

        # Build list files array
        files = []

        # Get list files but not file manager program
        for file in os.listdir("."):

            if str(file) == "matsimVoronoiGenerator.py":

                systemResponseMessage = "\n[INFO] Skipping matsimVoronoiGenerator.py file ...\n"
                self.systemResponse.text_color = "yellow"
                self.systemResponse.warn(systemResponseMessage)

            elif ".jpg" in str(file) or ".png" in str(file) or ".bmp" in str(file) or ".tiff" in str(file) or ".jpeg" in str(file):

                systemResponseMessage = "\n[INFO] File founded: " + str(file) + ".\n"
                self.systemResponse.text_color = "blue"
                self.systemResponse.info(systemResponseMessage)

                files.append(file)

        systemResponseMessage = "\n[INFO] " + str(len(files)) + " files founded.\n"
        self.systemResponse.text_color = "green"
        self.systemResponse.succeed(systemResponseMessage)

        return files

    # Function: getFileParameters
    def getFileParameters(self, file):

        fileSplit = file.split(".")
        extension = fileSplit[int(len(fileSplit)) - 1]

        # If is not a file and it´s a dir len no change
        if len(file) == len(extension):

            # Set as name
            fileName = extension

            # Set file extension as void
            fileExtension = ""

        else:
            # Set as name the file original name removing extension
            fileName = file.replace("." + str(extension), "")

            # Set file extension split
            fileExtension = extension

        return fileName, fileExtension

    # Function: buildFileDir
    def buildFileDir(self, fileName):

        try:
            # Get dir path
            dirPath = "./" + str(fileName)

            # Create dir
            os.mkdir(str(dirPath))

        except:
            systemResponseMessage = "\n[ERROR] Error building " + str(fileName) + " file dir.\n"
            self.systemResponse.text_color = "red"
            self.systemResponse.fail(systemResponseMessage)

    # Function: generateVoronoi
    def generateVoronoi(self, dataToSolve):

        img = cv2.cvtColor(dataToSolve, cv2.COLOR_BGR2GRAY)
        ret, img = cv2.threshold(img, 230, 255, cv2.THRESH_BINARY)

        cv2.imwrite("output.jpg", img)

        size = np.size(img)
        skel = np.zeros(img.shape, np.uint8)

        element = cv2.getStructuringElement(cv2.MORPH_CROSS, (3, 3))

        original = cv2.countNonZero(img)

        while True:
            open = cv2.morphologyEx(img, cv2.MORPH_OPEN, element)
            temp = cv2.subtract(img, open)
            eroded = cv2.erode(img, element)
            skel = cv2.bitwise_or(skel, temp)
            img = eroded.copy()

            actual = cv2.countNonZero(img)
            print("[INFO] Progress: " + str(actual) + "/" + str(original))

            if cv2.countNonZero(img) == 0:
                break

        dataSolved = skel

        return dataSolved

    # Function: saveDataSolved
    def saveDataSolved(self, fileName, fileExtension, dataSolved):

        # Get save path
        savePath = "./" + str(fileName) + "/" + str(fileName) + "Processed." + str(fileExtension)

        # Save data solved into file
        cv2.imwrite(savePath, dataSolved)

    # Function: processRequests
    def processRequests(self, files):

        print("\n**************************************************************************")
        print("Processing request:")
        print("**************************************************************************\n")

        if True:
            # Get initial time
            initialTime = datetime.datetime.now()

            # Prepare variable to count files processed
            numProcessed = 0

            # For each file process
            for file in files:

                # Increase numProcessed
                numProcessed = numProcessed + 1

                systemResponseMessage = "\n[INFO] Processing " + str(file) + ": " + str(numProcessed) + "/" + str(len(files))
                self.systemResponse.text_color = "blue"
                self.systemResponse.info(systemResponseMessage)

                # Extract file name and extension
                fileName, fileExtension = self.getFileParameters(file)

                # Build file dir
                self.buildFileDir(fileName)

                # Get data to solve
                dataToSolve = cv2.imread(str(file))

                # Generate Voronoi
                dataSolved = self.generateVoronoi(dataToSolve)

                # Save data solved into file
                self.saveDataSolved( fileName, fileExtension, dataSolved)

            systemResponseMessage = "\n[INFO] Request done correctly.\n"
            self.systemResponse.text_color = "green"
            self.systemResponse.succeed(systemResponseMessage)

            # Get end time
            endTime = datetime.datetime.now()

            # Compute elapsed time
            elapsedTime = endTime - initialTime

            systemResponseMessage = "\n[INFO] Elapsed time: " + str(elapsedTime) + ".\n"
            self.systemResponse.text_color = "blue"
            self.systemResponse.info(systemResponseMessage)


# Function: main
def main():

    print("**************************************************************************")
    print("**************************************************************************")
    print("                   Program: MATSim Voronoi Generator                      ")
    print("                     Author: David Velasco Garcia                         ")
    print("                             @davidvelascogarcia                          ")
    print("**************************************************************************")
    print("**************************************************************************")

    print("\nLoading MATSim Voronoi Generator engine ...\n")

    # Build matsimVoronoiGenerator object
    matsimVoronoiGenerator = MATSimVoronoiGenerator()

    # Get system platform
    systemPlatform, systemRelease = matsimVoronoiGenerator.getSystemPlatform()

    # Get root files
    files = matsimVoronoiGenerator.getRootFiles()

    # Process input requests
    matsimVoronoiGenerator.processRequests(files)

    print("**************************************************************************")
    print("Program finished")
    print("**************************************************************************")
    print("\nmatsimVoronoiGenerator program finished correctly.\n")

    #userExit = input()


if __name__ == "__main__":

    # Call main function
    main()