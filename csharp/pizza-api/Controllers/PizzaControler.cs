using ContosoPizza.Models;
using ContosoPizza.Services;
using Microsoft.AspNetCore.Mvc;

namespace ContosoPizza.Controllers;

[ApiController]
[Route("[controller]")]
public class PizzaController : ControllerBase
{
    public PizzaController()
    {
    }

    // GET all action
    [HttpGet]
    public ActionResult<List<Pizza>> GetAll() =>
        PizzaService.GetAll();

    // GET by Id action

    [HttpGet("{id}")]
    public ActionResult<Pizza> Get(int id)
    {
        var pizza = PizzaService.Get(id);
        if(pizza == null){
            return NotFound();
        }
        return pizza;
    }
        

    // POST action

    [HttpPost]
    public IActionResult Create(Pizza pizza)
    {
        PizzaService.Add(pizza);

        // Returns the HTTP Response as an IActionResult 
        return CreatedAtAction(nameof(Create), new { id = pizza.Id}, pizza);
    }

    // PUT action

    [HttpPut("{id}")]
    public IActionResult Update(int id, Pizza pizza)
    {
        // Test for some type of error

        if(id != pizza.Id)
            return BadRequest();

        var existingPizza = PizzaService.Get(id);

        // We first check whether or not the object exists

        if(existingPizza is null)
            return NotFound();
        
        // if the element exists and 
        PizzaService.Update(pizza);

        // Lastly, return a 204 Status Code to HTTP => success
        return NoContent();
    }

    // DELETE action

    [HttpDelete("{id}")]
    public IActionResult Delete(int id)
    {
        var deletePizza = PizzaService.Get(id);

        if(deletePizza is null)
            return NotFound();
        
        PizzaService.Delete(id);

        return NoContent();
    }
}