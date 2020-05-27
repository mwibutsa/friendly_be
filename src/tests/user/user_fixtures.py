create_user_mutation = """
mutation {{
    createUser(firstName: "{firstName}",
    lastName: "{lastName}",
    email: "{email}",
    password: "{password}",
    username: "{username}"){{
          firstName,
          lastName,
          email,
          username
          }}
}}
"""
