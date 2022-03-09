# -*- coding: utf-8 -*-

import arcpy


class Toolbox(object):
    def __init__(self):
        """Define the toolbox (the name of the toolbox is the name of the
        .pyt file)."""
        self.label = "Toolbox"
        self.alias = "toolbox"

        # List of tool classes associated with this toolbox
        self.tools = [Tool]


class Tool(object):
    def __init__(self):
        """Define the tool (tool name is the name of the class)."""
        self.label = "Geoprocessing Name Helper"
        self.description = "Assists in naming an output file for a geoprocessing tool."
        self.canRunInBackground = False

    def get_filename_options(self, shapefileName):
        # 1. covert spaces to underscores
        updateFileName = shapefileName.replace(" ", "_")
        # 2. return if less than acceptable length
        acceptFileNames = []
        if len(updateFileName) < 15:
            acceptFileNames.append(updateFileName)
        # 3. change underscores to camelCase
        fileNameList = updateFileName.split("_")
        fileNameList = [name[0].upper() + name[1:] for name in fileNameList]
        acceptFileNames.append("".join(fileNameList))
        return acceptFileNames

    def getParameterInfo(self):
        """Define parameter definitions"""
        param0 = arcpy.Parameter(
            displayName="Input Feature",
            name="in_features",
            datatype="GPFeatureLayer",
            parameterType="Required",
            direction="Input"
        )
        param1 = arcpy.Parameter(
            displayName="Raw Name String",
            name="raw_name_string",
            datatype="String",
            parameterType="Required",
            direction="Input"
        )
        param2 = arcpy.Parameter(
            displayName="Name Suggestions",
            name="name_sugg_dropdown",
            datatype="GPString",
            parameterType="Required",
            direction="Input",
            enabled=False,
            multiValue=True

        )
        params = [param0, param1, param2]
        return params

    def isLicensed(self):
        """Set whether tool is licensed to execute."""
        return True

    def updateParameters(self, parameters):
        """Modify the values and properties of parameters before internal
        validation is performed.  This method is called whenever a parameter
        has been changed."""
        # LOGIC TO BE ADDED:
        if parameters[1].valueAsText:
            parameters[2].enabled = True
            # call another method here to do the file name processing/shortening
            parameters[2].filter.list = self.get_filename_options(
                parameters[1].valueAsText)

        return

    def updateMessages(self, parameters):
        """Modify the messages created by internal validation for each tool
        parameter.  This method is called after internal validation."""
        return

    def execute(self, parameters, messages):
        """The source code of the tool."""
        arcpy.AddMessage("paramter1 {}".format(parameters[1].valueAsText))
        arcpy.AddMessage(dir(parameters[1]))
        return
