from typing import Dict,List
import requests
import os
import json

class ExonReader:
    def __init__(self) -> None:
        self.__exons = []

    def get_exons(self) -> List[int]:
        return self.__exons

    def __read_url(self, identifier) -> List[Dict]:
        server = "https://rest.ensembl.org"
        ext = f"/lookup/id/{identifier}?expand=1"
        headers = {"content-type" : "application/json"}
        response = requests.get(url=server + ext, headers=headers)

        if response.status_code == 200:
            response_json = response.json()
            return response_json["Exon"]
        else:
            raise Exception(f"ExonReader - {response.status_code} / identifier - {identifier}")

    def __processing_exons(self) -> None:
        for i in range(len(self.__exons)):
            st = self.__exons[i]["start"]
            end = self.__exons[i]["end"]
            self.__exons[i] = end - st + 1

    def read_exons(self, identifier) -> None:
        array = self.__read_url(identifier)
        self.__exons = array
        self.__processing_exons()

class SequenseExonReader:
    def __init__(self):
        self.__sequense = ""
        self.__extra = [0,0]

    def get_sequense(self) -> str:
        return self.__sequense

    def get_extra(self) -> List[int]:
        return self.__extra

    def __read_url(self, identifier, type_seq) -> str:
        server = "https://rest.ensembl.org"
        ext = f"/sequence/id/{identifier}?mask_feature=1;type={type_seq}"
        headers = {"content-type" : "application/json"}
        path_get = f"{os.getcwd()}\GET\SER_{identifier}.json"

        if not os.path.exists(path_get):
            response = requests.get(url=server + ext, headers=headers)
            response_json = response.json()

            filename = open(path_get,"w")
            filename.write(json.dumps(response_json))
            filename.close()
          
        response = open(path_get,"r")
        response_json = json.load(response)
        response.close()

        return response_json["seq"]

    def __processing_sequense(self, seq) -> str:
        seq = list(seq)
        self.__seq_st(seq)
        self.__seq_end(seq)
        return ''.join(seq)

    def __seq_st(self, seq) -> None:
        ind = 0
        while seq[ind].islower():
            seq[ind] = seq[ind].upper()
            ind += 1

    def __seq_end(self, seq) -> None:
        ind = len(seq) - 1
        while seq[ind].islower():
            seq[ind] = seq[ind].upper()
            ind -= 1

    def __processing_extra(self, seq) -> None:
        self.__extra_st(seq)
        self.__extra_end(seq)
    
    def __extra_st(self, seq) -> None:
        ind = 0
        while seq[ind].islower():
            self.__extra[0] += 1
            ind += 1

    def __extra_end(self, seq) -> None:
        ind = len(seq) - 1
        while seq[ind].islower():
            self.__extra[1] += 1
            ind -= 1

    def read_sequense(self, identifier) -> None:
        cdna = self.__read_url(identifier, "cdna")
        self.__processing_extra(cdna)
        sequence = self.__processing_sequense(cdna)
        self.__sequense = sequence 

class ProteinReader:
    def __init__(self) -> None:
        self.__sequense = ""

    def get_sequense(self) -> str:
        return self.__sequense

    def __read_url(self, identifier) -> str:
        url = f"https://rest.uniprot.org/uniprotkb/{identifier}.json"
        path_get = f"{os.getcwd()}\GET\PR_{identifier}.json"

        if not os.path.exists(path_get):
            response = requests.get(url=url)
            response_json = response.json()

            filename = open(path_get,"w")
            filename.write(json.dumps(response_json))
            filename.close()
          
        response = open(path_get,"r")
        response_json = json.load(response)
        response.close()
            
        return response_json["sequence"]["value"]

    def read_sequense(self, identifier) -> None:
        seq = self.__read_url(identifier)
        self.__sequense = seq 

class ProteinDomainReader:
    def __init__(self):
        self.__domains = {}

    def get_domains(self):
        return self.__domains

    def __read_url(self, identifier) -> List[Dict]:
        url = f"https://rest.uniprot.org/uniprotkb/{identifier}.json"
        path_get = f"{os.getcwd()}\GET\PDR_{identifier}.json"

        if not os.path.exists(path_get):
            response = requests.get(url=url)
            response_json = response.json()

            filename = open(path_get,"w")
            filename.write(json.dumps(response_json))
            filename.close()
          
        response = open(path_get,"r")
        response_json = json.load(response)
        response.close()

        return response_json["features"]

    def __processing_domains(self, domains) -> None:
        for i in range(1, len(domains)):
            if domains[i]["type"] == "Region":
                break
            
            st = int(domains[i]["location"]["start"]["value"])
            end = int(domains[i]["location"]["end"]["value"])
            description = domains[i]["description"]

            self.__domains[st] = [end, description]

    def read_domains(self, identifier) -> None:
        domains = self.__read_url(identifier)
        self.__processing_domains(domains)        