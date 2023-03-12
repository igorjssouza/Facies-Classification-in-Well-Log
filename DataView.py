"""
Created on Sat Mar  4 09:33:00 2023

@author: igor
"""
import folium
import pandas as pd

class DataView():
    """
    A class used to data view
    
    ...
    
    Attributes
    ----------
    df : data frame
        a fomart data which receive data
    
    Methods
    -------
    mark_well_postion_on_map
        Show the num-th wells on map
        
    well_loc
        Plot well on map
    
    """
    def __init__(self, df):
        """
        Parameters
        ----------
        df : Pandas data frame
            receive the well data.

        Returns
        -------
        None.

        """
        self.df = df
    
    def mark_well_postion_on_map(self, numWell):
        """
        Parameters
        ----------
        numWell : INT
            well's number selected on map.

        Returns
        -------
        data frame
            return the data frame based on well's number.

        """
        return self.df[len(self.df)-numWell:len(self.df)].reset_index(drop=True)
    
    
    def well_loc(self, zs=9):
        """Shows a map with well based on coordinates
        
        Parameters
        ----------
        zs : int, optional
            Zoom the image to show the wells on the map. The default is 7.

        Returns
        -------
        m : folium.folium.Map
            plot a map based on latitude and longitude.

        """
        mean_lat = self.df['lat'].mean()
        mean_long = self.df['lng'].mean()
        m = folium.Map(location=[mean_lat, mean_long], 
                       tiles="OpenStreetMap", 
                       zoom_start=zs, 
                       control_scale=True)
        
        for index, well_location in self.df.iterrows():
            folium.Marker([well_location['lat'], 
                           well_location['lng']],
                          popup= well_location['SitID']).add_to(m)
        return m
    
    def rename_features(self, feaature_name, name_before = "well-"):
        """Add a name before the name feature

        Parameters
        ----------
        feaature_name : str
            feature's name wich you wish to select to change.
        name_before : str, optional
            A pice of name tha you want to add in start of the feature. The default is "well-".

        Returns
        -------
        None.

        """
        for i in range(0,len(self.df[feaature_name])):
            self.df[feaature_name][i] = name_before + "{}".format(self.df[feaature_name][i])
            
    def select_data(self, well_name, sitID = 'SitID'):
        empty_df = []
        for name in well_name:
            empty_df.append(self.df[self.df[sitID] == name])
        return pd.concat(empty_df).reset_index(drop=True)
    

        
        
        
