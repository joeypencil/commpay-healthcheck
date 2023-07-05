import lib.api_manager as api_manager
import lib.constants as constants
import logging


def configure_logger() -> None:
    logging.basicConfig(level=logging.INFO)

    file_handler = logging.FileHandler('healthcheck_logs.txt')
    formatter = logging.Formatter('%(asctime)s - %(levelname)s: %(message)s')
    file_handler.setFormatter(formatter)

    logging.getLogger('').addHandler(file_handler)


def get_sites_data(api_manager: object) -> list:
    api_manager.get_commpay_sites_data()

    if not api_manager.is_last_api_call_ok():
        return list()

    sites_data = api_manager.get_response_as_list()
    sites = list()

    for site in sites_data:
        site_url = site['externalApplicationPath']

        if not site_url.startswith('http'):
            logging.warning(f'Ignored entry with URL "{site_url}"')
        else:
            logging.info(f'Obtained URL "{site_url}"')
            sites.append(site_url)

    return sites


def execute_healthcheck_on_sites(api_manager: object, sites: list) -> None:
    for site in sites:
        api_manager.get_commpay_healthcheck_for_site(site)

        if not api_manager.is_last_api_call_ok():
            logging.warning(f'{site}: {constants.HEALTHCHECK_FAILURE}')
            continue

        html = api_manager.get_response_as_raw()
        
        if all(substring in html for substring in constants.HTML_GOOD_HEALTH_ELEMENTS):
            logging.info(f'{site}: {constants.HEALTHCHECK_GOOD}')
        else:
            logging.info(f'{site}: {constants.HEALTHCHECK_BAD}')


if __name__ == '__main__':
    configure_logger()
    api_manager = api_manager.APIManager()
    sites = get_sites_data(api_manager)

    if not sites:
        logging.error('Could not get CommPay sites data. Check connection with VPN gateways.')
        exit(1)

    execute_healthcheck_on_sites(api_manager, sites)