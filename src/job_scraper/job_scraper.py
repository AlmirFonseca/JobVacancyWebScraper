import pandas as pd

from typing import List, Dict, Optional

from jobspy import scrape_jobs

# Dictionaries for mapping various terms to their standardized forms.
website_dict:dict = {
    "LinkedIn": "linkedin",
    "Indeed": "indeed",
    "Glassdoor": "glassdoor",
    "ZipRecruiter": "zip_recruiter"
}

job_type_dict:dict = {
    "Tempo integral": "fulltime",
    "Contrato": "contract",
    "Meio período": "parttime",
    "Temporário": "temporary",
    "Estágio": "internship",
    "Por dia": "perdiem",
    "Noturno": "nights",
    "De verão": "summer",
    "Voluntário": "volunteer",
    "Outros": "other"
}

country_dict:dict = {
    "Rio de Janeiro": "rio de janeiro, brazil",
    "São Paulo": "sao paulo, brazil",
    "Brasília": "brasilia, brazil",
    "Belo Horizonte": "belo horizonte, brazil",
    "Curitiba": "curitiba, brazil",
    "Porto Alegre": "porto alegre, brazil",
    "Recife": "recife, brazil",
    "Fortaleza": "fortaleza, brazil",
    "Salvador": "salvador, brazil",
    "Goiânia": "goiania, brazil",
    "Manaus": "manaus, brazil",
    "Belém": "belem, brazil",
    "Guarulhos": "guarulhos, brazil",
    "Campinas": "campinas, brazil",
    "São Luís": "sao luis, brazil",
    "São Gonçalo": "sao goncalo, brazil",
    "Maceió": "maceio, brazil",
    "Duque de Caxias": "duque de caxias, brazil",
    "Natal": "natal, brazil",
    "Teresina": "teresina, brazil",
    "São Bernardo do Campo": "sao bernardo do campo, brazil",
    "Nova Iguaçu": "nova iguacu, brazil",
    # Pode adicionar mais, mas sem a garantia de encontrar vagas para localidades menores
}

keywords_dict:dict = {
    "Python" : "Python", 
    "C" : "C", 
    "C++" : "C++", 
    "C#" : "C#", 
    "JavaScript" : "JavaScript", 
    "Java" : "Java", 
    "HTML" : "HTML", 
    "CSS" : "CSS",
    "PHP" : "PHP", 
    "SQL" : "SQL", 
    "Ruby" : "Ruby", 
    "Julia" : "Julia", 
    "SPARQL" : "SPARQL", 
    "Swift" : "Swift", 
    "TypeScript" : "TypeScript", 
    "R" : "R",

    "Sem experiência" : "sem experiencia",
    "Junior" : "estagio",
    "Pleno" : "fulltime",
    "Sênior" : "senior"
}

remote_options_dict:dict = {
    "Trabalho remoto": True,
    "Trabalho não remoto": False
}

class JobScraper():
    """Class to facilitate job scraping from various online platforms.

    Attributes:
        jobs (DataFrame): Stores the scraped job data.
        data_types (list): List of types of data that can be selected (e.g., site names, job types).
        available_options (dict): Dictionary storing available options for each data type.
        selected_options (dict): Dictionary to store user-selected options for scraping.

    Methods:
        transpose_from_dict(dict_to_transpose, keys): Transposes selected keys from a dictionary to their corresponding values.
        get_options(data_type): Retrieves available options for a given data type.
        set_options(data_type, values): Sets the user-selected options for a given data type.
        remove_options(data_type, values): Removes selected options for a given data type.
        get_jobs(num_jobs=20, offset=0): Scrapes jobs based on selected options and returns the results.
    """

    def __init__(self):
        """Initializes the JobScraper with default values."""

        self.job: Optional[pd.DataFrame] = None

        self.data_types: List[str] = ["site_names", "job_types", "locations", "keywords", "remote_options"]

        self.available_options: Dict[str, List[str]] = {
            "site_names": list(website_dict.keys()),
            "job_types": list(job_type_dict.keys()),
            "locations": list(country_dict.keys()),
            "keywords": list(keywords_dict.keys()),
            "remote_options": list(remote_options_dict.keys())
        }

        self.selected_options: Dict[str, List[str]] = {
            "site_names": [],
            "job_types": [],
            "locations": [],
            "keywords": [],
            "remote_options": []
        }

    def transpose_from_dict(self, dict_to_transpose: Dict[str, str], keys: List[str]) -> List[str]:
        """Transposes selected keys from a dictionary to their corresponding values used by the scraper.

        Args:
            dict_to_transpose (dict): The dictionary from which to transpose values.
            keys (list): A list of keys for which values need to be transposed.

        Returns:
            list: A list of values corresponding to the provided keys.
        """
        
        transposed_values = []
        
        for key in keys:
            value = dict_to_transpose.get(key, None)
            if value:
                transposed_values.append(dict_to_transpose[key])

        return transposed_values
    
    def get_options(self, data_type: str) -> Optional[List[str]]:
        """Retrieves available options for a given data type.

        Args:
            data_type (str): The type of data for which options are needed.

        Returns:
            list: A list of available options for the specified data type, or None if the data type is invalid.
        """

            
        if data_type not in self.data_types:
            return None
        
        return self.available_options.get(data_type, None)
    
    def set_options(self, data_type: str, values: List[str]) -> bool:
        """Sets the user-selected options for a given data type.

        Args:
            data_type (str): The type of data for which options are being set.
            values (list): The list of options to set for the given data type.

        Returns:
            bool: True if the options were successfully set, False otherwise.
        """
        
        # Check if the data type is valid and if the list of values is not empty
        if data_type not in self.data_types or not values:
            return False
        
        available_options = self.get_options(data_type)

        if not available_options:
            return False

        # For each value, check if it is a valid option and if it is not already selected        
        for value in values:
            if value not in available_options:
                return False
            
            if value not in self.selected_options[data_type]:
                self.selected_options[data_type].append(value)

        return True
    
    def remove_options(self, data_type: str, values: List[str]) -> bool:
        """Removes selected options for a given data type.

        Args:
            data_type (str): The type of data for which options are being removed.
            values (list): The list of options to remove for the given data type.

        Returns:
            bool: True if the options were successfully removed, False otherwise.
        """
            
        # Check if the data type is valid and if the list of values is not empty
        if data_type not in self.data_types or not values:
            return False
        
        available_options = self.get_options(data_type)

        if not available_options:
            return False
        
        # For each value, check if it is a valid option and if it is present before removing
        for value in values:
            if value not in available_options:
                return False
            
            if value in self.selected_options[data_type]:
                self.selected_options[data_type].remove(value)

        return True

    def get_jobs(self, num_jobs: int = 20, offset: int = 0, country: str = "brazil", verbose: bool = False) -> Optional[pd.DataFrame]:
        """Scrapes jobs based on selected options and returns the results.

        Args:
            num_jobs (int, optional): Number of jobs to retrieve. Defaults to 20.
            offset (int, optional): Offset for the job search results. Defaults to 0.

        Returns:
            DataFrame: A DataFrame containing the scraped job data, or None in case of an error.
        """

        try:
            # Execute the job scraping function with the selected options
            # Note: some options accept only one value, so we need to select the first element of the list
            search_data = {
                "site_name": self.transpose_from_dict(website_dict, self.selected_options["site_names"]),
                "job_type": self.transpose_from_dict(job_type_dict, self.selected_options["job_types"])[0],
                "search_term": " ".join(self.transpose_from_dict(keywords_dict, self.selected_options["keywords"])),
                "location": self.transpose_from_dict(country_dict, self.selected_options["locations"])[0],
                "results_wanted": num_jobs, # Be aware of the number of results, the higher the number, the higher the chance of being blocked (rotating proxy should work)
                # "country_indeed": 
                "is_remote": self.transpose_from_dict(remote_options_dict, self.selected_options["remote_options"])[0],
                "offset": offset,  # Search for more results if you don't find enough jobs
                "country_indeed": country
            }

            if verbose:
                if search_data["is_remote"]:
                    print("Buscando por vagas remotas ")
                else:
                    print(f"Buscando por ")

                print(f"{search_data['search_term']}, {search_data['job_type']} em {search_data['location']} no site(s) {search_data['site_name']}")

            jobs = scrape_jobs(
                site_name=search_data["site_name"],
                job_type=search_data["job_type"],
                search_term=search_data["search_term"],
                location=search_data["location"],
                results_wanted=search_data["results_wanted"],
                is_remote=search_data["is_remote"],
                offset=search_data["offset"],
                # proxy=proxy,
                country_indeed=search_data["country_indeed"],
            )
        except Exception as e:
            print(e)
            self.jobs = None
        
        else:
            self.jobs = jobs
        
        finally:
            return self.jobs
        

if __name__ == "__main__":

    # formatting for pandas
    pd.set_option("display.max_columns", None)
    pd.set_option("display.max_rows", None)
    pd.set_option("display.width", None)
    pd.set_option("display.max_colwidth", 50)  # set to 0 to see full job url / desc

    scraper = JobScraper()
    scraper.set_options("site_names", ["LinkedIn", "Indeed"])
    scraper.set_options("job_types", ["Tempo integral"])
    scraper.set_options("locations", ["Rio de Janeiro"])
    scraper.set_options("keywords", ["Python", "Sem experiência"])
    # scraper.set_options("keywords", ["Python"])
    scraper.set_options("remote_options", ["Trabalho remoto"])
    scraper.get_jobs(verbose=True)
    print(scraper.jobs)
